from yattag import Doc
import requests

STYLE = """
<head><style>
.button-container {
    display: flex;
    height: 98vh;
}
button.split {
    flex: 1;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #3498db; /* Set your desired background color */
    color: #fff; /* Set your desired text color */
    cursor: pointer;
    transition: background-color 0.3s;
    font-size: 50;
}
button.split:hover {
    background-color: #2980b9; /* Set a different color for the hover effect */
}
table {
    border-collapse: collapse;
    width: 100%;
}
th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
    width: 1000px;
}
th {
    background-color: #f2f2f2;
}
button.button_in_table {
    width: 100%;
    box-sizing: border-box;
    border: 0;
}
button.add_button {
    width: 100%;
    flex: 1;
    padding: 10px;
    text-align: center;
}
div.page_buttons {
    display: flex;
    flex: 1;
    flex-direction: row;
    flex-wrap: wrap;
}
button.page_button {
    width: 50%;
    padding: 10px;
    text-align: center;
}
</style></head>
"""
SCRIPT = """
<script>
function remove_element(table_name, id) {
    fetch(`http://127.0.0.1:8000/${table_name}/${id}`, {
        method: 'DELETE', 
    });
}
function edit_element(table_name, id, content) {
    fetch(`http://127.0.0.1:8000/${table_name}/${id}`, {
        method: 'PUT', 
        headers: { 'Content-Type': 'application/json', },
        body: JSON.stringify(content),
    });
}
function add_element(table_name, content) {
    fetch(`http://127.0.0.1:8000/${table_name}/`, {
        method: 'POST', 
        headers: { 'Content-Type': 'application/json', },
        body: JSON.stringify(content),
    });
}
function go_to_page(table_name, page_number) {
    if (page_number == 0) {
        return;
    }
    window.location.replace(`http://127.0.0.1:8000/homepage/${table_name}?p=${page_number}`);
}
function add_button_handler(table_name) {
    const add_line = document.getElementById('add');
    const input_data_cells = add_line.querySelectorAll(`[hascontent]`);
    let data = {}
    input_data_cells.forEach(cell => {
        data[cell.id] = cell.children[0].value;
    });
    add_element(table_name, data);
    window.location.reload();
}
function remove_button_handler(table_name, id) {
    remove_element(table_name, id);
    window.location.reload();
}
function done_button_handler(table_name, id) {
    const line = document.getElementById(id);
    const editable_cells = line.querySelectorAll(`[editable='True']`);
    let new_data = {}
    editable_cells.forEach(cell => {
        new_data[cell.id] = cell.children[0].value;
    });
    const non_edited_cells = line.querySelectorAll(`[editable='False']`);
    non_edited_cells.forEach(cell => {
        new_data[cell.id] = cell.innerHTML;
    });
    edit_element(table_name, id, new_data);
    window.location.reload();
}
function edit_button_handler(table_name, id) {
    const line = document.getElementById(id);
    const editable_cells = line.querySelectorAll(`[editable='True']`);
    editable_cells.forEach(cell => {
        const content = cell.textContent;
        let input_cell = document.createElement('input');
        input_cell.type = 'text';
        input_cell.value = content;
        input_cell.id = cell.id;
        cell.innerHTML = '';
        cell.appendChild(input_cell);
    });
    const spot = line.querySelector('#edit_button_spot');
    const self = spot.querySelector('#edit_button');
    let done_button = document.createElement('button');
    done_button.innerHTML = 'done';
    done_button.setAttribute('class', 'button_in_table');
    done_button.setAttribute('onclick', `done_button_handler('${table_name}', ${id})`);
    spot.appendChild(done_button);
    self.remove();
}
</script>
"""
TABLE_DISPLAY_EDIT_POLICY = {
    "laptops": (
        ("id", False),
        ("model", False),
        ("cpu", False),
        ("gpu", False),
        ("screen_size", False),
        ("memory", False),
    ),
    "producers": (
        ("id", False),
        ("name", False),
        ("country", True),
        ("place", True),
        ("guarantee", True),
    ),
    "market_offers": (
        ("id", False),
        ("volume", True),
        ("cost", True),
        ("date", False),
        ("laptop_id", False),
        ("producer_id", False),
    ),
}


def homepage():
    doc, tag, text = Doc().tagtext()
    with tag("html"):
        doc.asis(STYLE)
        with tag("body"):
            with tag("div", klass="button-container"):
                for table_name in TABLE_DISPLAY_EDIT_POLICY:
                    with tag(
                        "button", onclick=f'window.open("{table_name}")', klass="split"
                    ):
                        text(table_name)

    return doc.getvalue()


def get_table(table_name, page_number):
    limit = 20
    skip = (page_number - 1) * limit
    return requests.get(
        f"http://127.0.0.1:8000/{table_name}?skip={skip}&limit={limit}"
    ).json()


def tablepage(table_name, page_number: int):
    doc, tag, text = Doc().tagtext()
    with tag("html"):
        doc.asis(STYLE)
        with tag("body"):
            doc.asis(SCRIPT)
            with tag("table"):
                with tag("tr"):
                    is_editable = any(
                        edit_policy
                        for _, edit_policy in TABLE_DISPLAY_EDIT_POLICY[table_name]
                    )
                    for column_name, _ in TABLE_DISPLAY_EDIT_POLICY[table_name]:
                        with tag("th"):
                            text(column_name)
                    if is_editable:
                        with tag("th"):
                            pass
                    with tag("th"):
                        pass
                for element in get_table(table_name, page_number):
                    with tag("tr", id=element["id"]):
                        for column_name, edit_policy in TABLE_DISPLAY_EDIT_POLICY[
                            table_name
                        ]:
                            with tag("td", id=column_name, editable=edit_policy):
                                text(element[column_name])
                        if is_editable:
                            with tag("td", id="edit_button_spot"):
                                with tag(
                                    "button",
                                    klass="button_in_table",
                                    id="edit_button",
                                    onclick=f"edit_button_handler('{table_name}', {element['id']})",
                                ):
                                    text("edit")
                        with tag("td"):
                            with tag(
                                "button",
                                klass="button_in_table",
                                onclick=f"remove_button_handler('{table_name}', {element['id']})",
                            ):
                                text("remove")

                with tag("tr", id="add"):
                    for column_name, _ in TABLE_DISPLAY_EDIT_POLICY[table_name]:
                        if column_name == "id":
                            with tag("td"):
                                pass
                            continue
                        with tag("td", hascontent="", id=column_name):
                            doc.stag("input", type="text")
                    if is_editable:
                        with tag("td"):
                            pass
                    with tag("td"):
                        pass
            with tag(
                "button",
                klass="add_button",
                onclick=f"add_button_handler('{table_name}')",
            ):
                text("add")
            with tag("div", "page_buttons"):
                with tag(
                    "button",
                    klass="page_button",
                    onclick=f"go_to_page('{table_name}', {page_number} - 1)",
                ):
                    text("<<")
                with tag(
                    "button",
                    klass="page_button",
                    onclick=f"go_to_page('{table_name}', {page_number} + 1)",
                ):
                    text(">>")
    return doc.getvalue()
