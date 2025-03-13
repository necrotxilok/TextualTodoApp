"""
An App to create a list of todos made with textual.
"""

import os
import json
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Label, SelectionList, Input
from textual.widgets.selection_list import Selection

class TodoApp(App):

	items = []
	highlighted = -1
	editItem = None

	CSS = """
	Screen {
		align: center middle;
	}
	Label {
		padding: 1;
		width: 80%;
		background: $accent;
		color: $background;
		text-align: center;
	}
	SelectionList {
		padding: 1;
		border: solid $accent;
		width: 80%;
		height: 70%;
	}
	Input {
		border: solid $accent;
		width: 80%;
		display: none;
	}
	"""

	BINDINGS = [
		("a", "add_item", "Add Item"),
		("e", "edit_item", "Edit Item"),
		("r", "remove_item", "Remove Item"),
		("q", "quit_app", "Quit"),
		("escape", "blur")
	]

	# Textual Compose
	# -------------------------------------------

	def compose(self) -> ComposeResult:
		self.log('Composed!!')
		"""Create child widgets for the app."""
		yield Header()
		yield Label("My Textual Todo App")
		yield SelectionList[int](*self.items, id="todoList")
		yield Input(placeholder="New Task" , id="inputTask")
		yield Footer()


	# Textual Events
	# -------------------------------------------

	def on_mount(self) -> None:
		self.log('Mounted!!')
		self.load_data()
		self.log(self.items)
		self.render_tasks()

	def on_selection_list_selection_highlighted(self, current):
		self.log('SelectionList Highlighted!!')
		self.log(current)
		self.log(current.selection_index)
		self.highlighted = current.selection_index
		#self.log(self.items[index])

	def on_selection_list_selection_toggled(self, current):
		self.log('SelectionList Selection Toggle!!')
		self.log(current)
		self.log(current.selection_index)
		idx = current.selection_index
		item = self.items[idx]
		done = not item[2]
		newItem = (item[0], idx, done)
		self.items[idx] = newItem
		self.save_data()

	def on_input_submitted(self, submitted):
		self.log('Input Submitted!!')
		self.log(submitted)
		self.log(submitted.value)
		if submitted.value:
			if (self.editItem == None):
				idx = len(self.items)
				newItem = (submitted.value, idx, False)
				self.items.append(newItem)
			else:
				editItem = self.editItem
				idx = editItem[1]
				done = editItem[2]
				newItem = (submitted.value, idx, done)
				self.items[idx] = newItem
		self.editItem = None
		inputTask = self.query_one("#inputTask")
		inputTask.styles.display = 'none'
		inputTask.clear()
		self.render_tasks()
		self.save_data()


	# Textual Actions
	# -------------------------------------------

	def _action_quit_app(self):
		self.exit()

	def _action_add_item(self):
		self.log('Add Item Action')
		self.render_input('')

	def _action_edit_item(self):
		self.log('Edit Item Action')
		idx = self.highlighted
		if (idx >= 0 and idx < len(self.items)):
			#selectionList = self.query_one("#todoList")
			#self.log(selectionList)
			editItem = self.items[idx]
			task = editItem[0]
			done = editItem[2]
			self.editItem = (task, idx, done)
			self.render_input(task)

	def _action_remove_item(self):
		self.log('Remove Item Action')
		idx = self.highlighted
		if (idx >= 0 and idx < len(self.items)):
			del self.items[idx]
			self.render_tasks()
			self.save_data()

	def action_blur(self) -> None:
		inputTask = self.query_one("#inputTask")
		inputTask.styles.display = 'none'
		inputTask.clear()
		self.render_tasks()


	# Custom functions
	# -------------------------------------------

	def load_data(self):
		if not os.path.isfile('todo.json'):
			return
		with open('todo.json', 'r') as file:
			data = json.load(file)
		self.items = []
		for i, item in enumerate(data):
			self.items.append((item.get('task'), i, item.get('done')))

	def save_data(self):
		data = []
		for i, item in enumerate(self.items):
			data.append({
				"task": item[0],
				"done": item[2]
			})
		with open('todo.json', 'w') as f:
			json.dump(data, f)
	
	def render_tasks(self):
		selectionList = self.query_one("#todoList")
		selectionList.disabled = False
		selectionList.clear_options()
		selectionList.add_options(self.items)
		selectionList.focus()

	def render_input(self, value):
		inputTask = self.query_one("#inputTask")
		inputTask.styles.display = 'block'
		inputTask.value = value
		inputTask.focus()
		selectionList = self.query_one("#todoList")
		selectionList.disabled = True



if __name__ == "__main__":
	app = TodoApp()
	app.run()
