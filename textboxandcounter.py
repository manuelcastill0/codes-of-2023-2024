#i got guidence from the links that are in the assignment and the code you showed in class

import flet as ft

def main(page: ft.Page):
    def textbox_changed(e):
        text.value = e.control.value
        text.color = "Cyan"
        word_count.value = f"Word count: {len(text.value.split())}"
        page.update()

    def pick_files_result(e: ft.FilePickerResultEvent):
        print(e.files)
        print(e.path)
        selected_files.value = e.path

    def save_file_result(e: ft.FilePickerResultEvent):
        with open(e.path, "w") as f:
            f.write(text.value)
        save_file.value = f"Saved to: {e.path}"
        page.update()

    def new_file_result(e: ft.FilePickerResultEvent):
        new_file.value = f"New file: {e.path}"
        page.update()

    text = ft.Text(value="", color="black")
    txtbox = ft.TextField(
        label="Textbox:",
        on_change=textbox_changed,
        multiline=True
    )

    word_count = ft.Text(value="Word count: 0", color="white")
    page.add(txtbox, text, word_count)

    selected_files = ft.Text(value="", color="black")
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    save_file = ft.Text(value="", color="black")
    save_file_dialog = ft.FilePicker(on_result=save_file_result)
    page.overlay.append(save_file_dialog)

    new_file = ft.Text(value="", color="black")
    new_file_dialog = ft.FilePicker(on_result=new_file_result)
    page.overlay.append(new_file_dialog)

    page.add(selected_files, save_file, new_file)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Select File",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _:pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
                ft.ElevatedButton(
                    "New File",
                    icon=ft.icons.CREATE_NEW_FOLDER,
                    on_click=new_file_dialog.pick_files,
                ),
                ft.ElevatedButton(
                    "Save File",
                    icon=ft.icons.SAVE_AS,
                    on_click=save_file_dialog.save_file,
                ),
            ]    
        )
    )

ft.app(target=main)