from tkinter import Button

import flet
from flet import *
from flet import icons, padding, alignment, colors, border_radius


# Checkbox(label=new_task.value)
# Container(
#                 content=Checkbox(label=new_task.value),
#                 alignment=alignment.center,
#                 width=50,
#                 height=50,
#                 bgcolor=colors.AMBER,
#                 border_radius=border_radius.all(5),
#             ),


class Task(UserControl):
    def __init__(self, task_name, task_delete):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete

    def build(self):
        self.display_task = Checkbox(value=False, label=self.task_name)
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        # IconButton(
                        #     icon=icons.CREATE_OUTLINED,
                        #     tooltip="Edit To-Do",
                        #     on_click=self.edit_clicked,
                        # ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)


class TodoApp(UserControl):
    def build(self):
        self.new_task = TextField(hint_text="Whats needs to be done?", expand=True)
        self.test_task = TextField(hint_text="Whats needs to be done?", expand=True)

        self.tasks = Column()

        # application's root control (i.e. "view") containing all other controls
        return Column(
            width=600,
            controls=[
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)

        item = Refer_Card(self.new_task.value, self.task_delete, self.new_task.value,
                          self.task_delete, self.new_task.value)

        self.tasks.controls.append(item)

        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()


class Refer_Card(UserControl):
    def __init__(self, ref_name, ref_type, ref_numb, ref_time, ref_com, task_delete):
        super().__init__()
        self.ref_name = ref_name
        self.ref_type = ref_type
        self.ref_numb = ref_numb
        self.ref_time = ref_time
        self.ref_com = ref_com

        self.task_delete = task_delete

    def build(self):
        self.text_ref_name = Text(self.ref_name)
        self.text_ref_type = Text(self.ref_type)
        self.text_ref_numb = Text(self.ref_numb)
        self.text_ref_time = Text(self.ref_time)
        self.text_ref_com = Text(self.ref_com)

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[

                Row(
                    spacing=0,
                    controls=[
                        # IconButton(
                        #     icon=icons.CREATE_OUTLINED,
                        #     tooltip="Edit To-Do",
                        #     on_click=self.edit_clicked,
                        # ),
                        self.text_ref_name,
                        self.text_ref_type,
                        self.text_ref_numb,
                        self.text_ref_time,
                        self.text_ref_com,
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )
        return Column(alignment="spaceBetween", controls=[Card(content=Container(content=self.display_view))])

    def delete_clicked(self, e):
        self.task_delete(self)

    # def edit_clicked(self, e):
    #     self.edit_name.value = self.display_task.label
    #     self.display_view.visible = False
    #     self.update()
    #
    # def save_clicked(self, e):
    #     self.display_task.label = self.edit_name.value
    #     self.display_view.visible = True
    #     self.edit_view.visible = False
    #     self.update()
    #
    # def delete_clicked(self, e):
    #     self.task_delete(self)


class MainApp(UserControl):
    def build(self):
        self.refer_name = TextField(label="Название", expand=True)
        self.refer_type = Dropdown(
            label="Тип переадресации",
            options=[
                dropdown.Option("Безусловная"),
                dropdown.Option("Занято"),
                dropdown.Option("Нет ответа"),
                dropdown.Option("Отклонено"),
            ], )

        self.refer_nomber = TextField(label="Номер на который переадресовать", expand=True, keyboard_type="number")
        self.refer_timetable = Dropdown(
            label="Расписание",
            options=[
                dropdown.Option("Любое время"),
                dropdown.Option("Рабочие часы"),
                dropdown.Option("Вне рабочие часы"),
                dropdown.Option("Ручной ввод"),
            ], )

        self.refer_comment = TextField(label="Комментарии", expand=True)
        self.tasks = Column([Divider(height=10)])

        # application's root control (i.e. "view") containing all other controls
        return Column(
            width=800,
            controls=[
                Row(
                    controls=[
                        self.refer_name,
                        self.refer_type,
                    ],
                ),
                Row(
                    controls=[
                        self.refer_nomber,
                        self.refer_timetable
                    ],
                ),
                Row(
                    controls=[
                        self.refer_comment,
                        FloatingActionButton(
                            icon=icons.DONE,
                            bgcolor=colors.PINK,
                            on_click=self.add_clicked),
                    ],
                ),
                self.tasks

            ],
        )

    def add_clicked(self, e):
        ref_nam = self.refer_name.value
        ref_typ = self.refer_type.value
        ref_num = self.refer_nomber.value
        ref_tim = self.refer_timetable.value
        ref_com = self.refer_comment.value

        if ref_nam != "" and ref_typ != "" and ref_num != "" and ref_tim != "":
            item = Refer_Card(ref_nam, ref_typ, ref_num, ref_tim, ref_com, self.task_delete)

            self.tasks.controls.append(item)
            self.refer_name.value = ""
            self.refer_type.value = ""
            self.refer_nomber.value = ""
            self.refer_timetable.value = ""
            self.refer_comment.value = ""

            self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()





def main(page: Page):
    def button_click(e):
        todo = MainApp()
        page.add(todo)
        page.update()


    page.add(ElevatedButton("Do some lengthy task!", on_click=button_click))

    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    # page.theme_mode = "dark"
    # page.theme = theme.Theme(color_scheme_seed="green")


    page.update()


flet.app(target=main)
