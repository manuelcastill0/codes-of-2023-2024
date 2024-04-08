import flet as ft
 
class estudiante(ft.UserControl):
    def __init__(self, name, points):
        self.name = name
        self.points = points
 
    def build(self):
        info = ft.Text(value=f"{self.name}: {self.points} points remaining")
        return info
 
def main(page: ft.Page):
    names = ['Manuel Jesus', 'Alejandro', 'Reilly', 'Hans', 'Manuel Liriano', 'Jeudry', 'Yury',
             'Daniela Cabrera', 'Daniela Sofia', 'Nicolas', 'Roxi', 'Fabrianny', 'Felix', 'Marcos',
             'Joaquin', 'Juan', 'Jadeline', 'Chrismerlis', 'Camila', 'Shelsie' , 'Emmanuel', 'Paolo',
             'Brittney']
    scores = {name: 100 for name in names}
 
    def textbox_changed(e):
        input_text = e.control.value
        for name in names:
            if name == input_text:
                scores[name] -= 5
                page.add(ft.Text(f"{name}: {scores[name]} points remaining"))
                with open('puntos_restantes.txt', 'w') as f:
                    for name, points in scores.items():
                        f.write(f"{name}: {points} points remaining\n")
                break
 
    tb = ft.TextField(
        label="Enter a name:",
        on_change=textbox_changed,
    )
    page.add(tb)

    def save_file_result(e: ft.FilePickerResultEvent):
            with open(e.path, "w") as f:
                f.write(tb.value)
            save_file.value = f"Saved to: {e.path}"
            page.update()

    save_file = ft.Text(value="", color="white")
    save_file_dialog = ft.FilePicker(on_result=save_file_result)
    page.overlay.append(save_file_dialog)

    page.add(save_file,ft.ElevatedButton("Save", on_click=save_file_result))
    

ft.app(target=main)