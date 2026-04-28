import tkinter as tk
from itertools import combinations
from tkinter import messagebox
from tkinter import ttk


class FootballTeamApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Football Team Balancer")
		self.base_font = ("Arial", 12)
		self.bold_font = ("Arial", 12, "bold")
		self.button_font = ("Arial", 12, "bold")
		self.level_values = [""] + [str(value) for value in self._build_level_values()]
		self.level_columns_visible = True
		self.default_players = [
			("Tomek S", "", "Marcin M", ""),
			("Marcin Sz", "", "Mateusz N", ""),
			("Milosz", "", "Lukasz Is", ""),
			("Bogus", "", "Rafal", ""),
			("Sebastian", "", "Michal S", ""),
			("Obecny", "", "Mateusz K", ""),
		]
		self.entries = []
		self.configure_styles()
		self.create_table()
		self.create_process_button()
		self.create_sum_labels()

	def _build_level_values(self):
		return [step / 2 for step in range(2, 21)]

	def configure_styles(self):
		style = ttk.Style()
		style.configure("Header.TLabel", font=self.bold_font, background="#e0e0e0", anchor="center")
		style.configure("Id.TLabel", font=self.base_font, background="#f0f0ff", anchor="center")
		style.configure("Info.TLabel", font=self.bold_font, anchor="center")
		style.configure("Big.TButton", font=self.button_font, padding=(7, 5), anchor="center")
		style.configure(
			"Team1.TCombobox",
			font=self.base_font,
			fieldbackground="#d0eaff",
			background="#d0eaff",
		)
		style.map("Team1.TCombobox", fieldbackground=[("readonly", "#d0eaff")])
		style.map("Team1.TCombobox", justify=[("readonly", "center")])
		style.configure(
			"Team2.TCombobox",
			font=self.base_font,
			fieldbackground="#fff9cc",
			background="#fff9cc",
		)
		style.map("Team2.TCombobox", fieldbackground=[("readonly", "#fff9cc")])
		style.map("Team2.TCombobox", justify=[("readonly", "center")])

	def create_table(self):
		columns = ["id", "Team 1", "Level", "Team 2", "Level", "id"]
		self.header_labels = []
		for col, col_name in enumerate(columns):
			label = ttk.Label(self.root, text=col_name, style="Header.TLabel")
			label.grid(row=0, column=col, padx=2, pady=2, sticky="nsew")
			self.header_labels.append(label)

		self.entries = []
		for row in range(1, 11):
			row_entries = []
			id_label1 = ttk.Label(self.root, text=str(row), style="Id.TLabel")
			id_label1.grid(row=row, column=0, padx=1, pady=1, sticky="nsew")
			row_entries.append(None)

			team1_name = tk.Entry(self.root, width=12, bg="#d0eaff", font=self.base_font, justify="center")
			team1_name.grid(row=row, column=1, padx=1, pady=1)
			row_entries.append(team1_name)

			team1_level = ttk.Combobox(
				self.root,
				width=5,
				values=self.level_values,
				state="readonly",
				style="Team1.TCombobox",
				font=self.base_font,
				justify="center",
			)
			team1_level.grid(row=row, column=2, padx=1, pady=1)
			team1_level.bind("<<ComboboxSelected>>", self.update_sums)
			row_entries.append(team1_level)

			team2_name = tk.Entry(self.root, width=12, bg="#fff9cc", font=self.base_font, justify="center")
			team2_name.grid(row=row, column=3, padx=1, pady=1)
			row_entries.append(team2_name)

			team2_level = ttk.Combobox(
				self.root,
				width=5,
				values=self.level_values,
				state="readonly",
				style="Team2.TCombobox",
				font=self.base_font,
				justify="center",
			)
			team2_level.grid(row=row, column=4, padx=1, pady=1)
			team2_level.bind("<<ComboboxSelected>>", self.update_sums)
			row_entries.append(team2_level)

			id_label2 = ttk.Label(self.root, text=str(row), style="Id.TLabel")
			id_label2.grid(row=row, column=5, padx=1, pady=1, sticky="nsew")
			row_entries.append(None)
			self.entries.append(row_entries)

			if row <= len(self.default_players):
				default_team1_name, default_team1_level, default_team2_name, default_team2_level = self.default_players[row - 1]
				team1_name.insert(0, default_team1_name)
				team1_level.set(default_team1_level)
				team2_name.insert(0, default_team2_name)
				team2_level.set(default_team2_level)

	def create_process_button(self):
		self.process_btn = ttk.Button(self.root, text="Balance Teams", command=self.process_teams, style="Big.TButton", width=14)
		self.process_btn.grid(row=11, column=1, columnspan=1, pady=(8, 2), sticky="w")
		self.toggle_levels_btn = ttk.Button(self.root, text="Hide Levels", command=self.toggle_level_columns, style="Big.TButton", width=14)
		self.toggle_levels_btn.grid(row=12, column=1, columnspan=1, pady=(4, 2), sticky="w")

	def create_sum_labels(self):
		self.sum1_label = ttk.Label(self.root, text="Sum:", style="Info.TLabel")
		self.sum1_label.grid(row=11, column=2)
		self.sum2_label = ttk.Label(self.root, text="Sum:", style="Info.TLabel")
		self.sum2_label.grid(row=11, column=4)
		self.diff_label = ttk.Label(self.root, text="Difference:", style="Info.TLabel")
		self.diff_label.grid(row=11, column=3)
		self.sum1_val = ttk.Label(self.root, text="0.0", style="Info.TLabel")
		self.sum1_val.grid(row=12, column=2)
		self.sum2_val = ttk.Label(self.root, text="0.0", style="Info.TLabel")
		self.sum2_val.grid(row=12, column=4)
		self.diff_val = ttk.Label(self.root, text="0.0", style="Info.TLabel")
		self.diff_val.grid(row=12, column=3)
		self.update_sums()

	def toggle_level_columns(self):
		level_widgets = [self.header_labels[2], self.header_labels[4], self.sum1_label, self.sum1_val, self.sum2_label, self.sum2_val]
		for row_entries in self.entries:
			level_widgets.extend([row_entries[2], row_entries[4]])

		if self.level_columns_visible:
			for widget in level_widgets:
				widget.grid_remove()
			self.toggle_levels_btn.config(text="Show Levels")
		else:
			for widget in level_widgets:
				widget.grid()
			self.toggle_levels_btn.config(text="Hide Levels")

		self.level_columns_visible = not self.level_columns_visible

	def update_sums(self, event=None):
		sum1 = 0.0
		sum2 = 0.0
		for row_entries in self.entries:
			team1_level = row_entries[2].get().strip()
			team2_level = row_entries[4].get().strip()
			if team1_level:
				sum1 += float(team1_level)
			if team2_level:
				sum2 += float(team2_level)
		self.sum1_val.config(text=f"{sum1:.2f}")
		self.sum2_val.config(text=f"{sum2:.2f}")
		self.diff_val.config(text=f"{abs(sum1 - sum2):.2f}")

	def get_player_data(self):
		players = []
		for row_entries in self.entries:
			for name_index, level_index in ((1, 2), (3, 4)):
				name = row_entries[name_index].get().strip()
				level_text = row_entries[level_index].get().strip()
				if not name and not level_text:
					continue
				if not name or not level_text:
					raise ValueError("Each player must have both a name and a level.")
				players.append((name, float(level_text)))
		return players

	def balance_players(self, players):
		team_size = len(players) // 2
		total_level = sum(level for _, level in players)
		best_indices = None
		best_difference = None
		for selected_indices in combinations(range(len(players)), team_size):
			selected_set = set(selected_indices)
			team1_sum = sum(players[index][1] for index in selected_set)
			team2_sum = total_level - team1_sum
			difference = abs(team1_sum - team2_sum)
			if best_difference is None or difference < best_difference:
				best_difference = difference
				best_indices = selected_set
				if difference == 0:
					break
		team1 = [players[index] for index in range(len(players)) if index in best_indices]
		team2 = [players[index] for index in range(len(players)) if index not in best_indices]
		return team1, team2

	def clear_table(self):
		for row_entries in self.entries:
			row_entries[1].delete(0, tk.END)
			row_entries[2].set("")
			row_entries[3].delete(0, tk.END)
			row_entries[4].set("")

	def populate_balanced_teams(self, team1, team2):
		for row_index, player in enumerate(team1):
			self.entries[row_index][1].insert(0, player[0])
			self.entries[row_index][2].set(self.format_level(player[1]))
		for row_index, player in enumerate(team2):
			self.entries[row_index][3].insert(0, player[0])
			self.entries[row_index][4].set(self.format_level(player[1]))

	def format_level(self, level):
		return str(int(level)) if float(level).is_integer() else f"{level:.1f}"

	def process_teams(self):
		try:
			players = self.get_player_data()
		except ValueError as error:
			messagebox.showerror("Invalid data", str(error))
			return
		if not players or len(players) < 2:
			messagebox.showwarning("Too few players", "Enter at least two players before balancing.")
			return
		if len(players) % 2 != 0:
			messagebox.showerror(
				"Equal team sizes required",
				"The total number of players must be even so both teams have the same number of players.",
			)
			return
		team1, team2 = self.balance_players(players)
		self.clear_table()
		self.populate_balanced_teams(team1, team2)
		self.update_sums()
		team1_sum = sum(level for _, level in team1)
		team2_sum = sum(level for _, level in team2)
		messagebox.showinfo(
			"Info",
			"Teams balanced with {} players per team. Difference: {:.2f}".format(
				len(team1), abs(team1_sum - team2_sum)
			),
		)


if __name__ == "__main__":
	root = tk.Tk()
	app = FootballTeamApp(root)
	root.mainloop()
