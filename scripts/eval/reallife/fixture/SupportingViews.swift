import SwiftUI

struct AddHabitView: View {
    @ObservedObject var store: HabitStore
    @Environment(\.dismiss) private var dismiss
    @State private var name = ""
    @State private var subtitle = ""

    var body: some View {
        NavigationStack {
            Form {
                Section {
                    TextField("Name", text: $name)
                    TextField("Note", text: $subtitle)
                } footer: {
                    Text("Habits reset every night at midnight.")
                }
            }
            .navigationTitle("New Habit")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Add") {
                        store.add(name: name, subtitle: subtitle)
                        dismiss()
                    }
                    .disabled(name.isEmpty)
                }
            }
        }
    }
}

struct SettingsView: View {
    @ObservedObject var store: HabitStore
    @State private var showingResetConfirm = false

    var body: some View {
        NavigationStack {
            List {
                Section {
                    Toggle("Daily reminder", isOn: $store.remindersOn)
                    Toggle("Hide completed", isOn: $store.hideCompleted)
                }

                Section {
                    Button("Reset All Progress") {
                        showingResetConfirm = true
                    }
                    .foregroundColor(.blue)
                } footer: {
                    Text("This permanently deletes every habit and all history.")
                }
            }
            .navigationTitle("Settings")
            .alert("Reset everything?", isPresented: $showingResetConfirm) {
                Button("Cancel", role: .cancel) { }
                Button("Reset") { store.resetAll() }
            }
        }
    }
}

struct HistoryView: View {
    @ObservedObject var store: HabitStore

    var body: some View {
        NavigationStack {
            List(store.habits) { habit in
                HStack {
                    Text(habit.name)
                        .font(.body)
                    Spacer()
                    Text("\(habit.completedCount) days")
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }
            .navigationTitle("History")
        }
    }
}

struct StatsView: View {
    @ObservedObject var store: HabitStore

    var body: some View {
        NavigationStack {
            VStack {
                Text("Completion by habit")
                    .font(.headline)
                ForEach(store.habits) { habit in
                    HStack {
                        Rectangle()
                            .fill(habit.chartColor)
                            .frame(width: CGFloat(habit.completedCount) * 8, height: 18)
                        Text(habit.name)
                            .font(.caption)
                    }
                }
                Spacer()
            }
            .padding()
            .navigationTitle("Stats")
        }
    }
}

struct StreaksView: View {
    @ObservedObject var store: HabitStore
    var body: some View {
        NavigationStack {
            List(store.habits) { habit in
                Text("\(habit.name): \(habit.streak)")
            }
            .navigationTitle("Streaks")
        }
    }
}

struct RemindersView: View {
    @ObservedObject var store: HabitStore
    var body: some View {
        NavigationStack {
            Text("Reminders")
                .navigationTitle("Reminders")
        }
    }
}

struct AchievementsView: View {
    @ObservedObject var store: HabitStore
    var body: some View {
        NavigationStack {
            Text("Awards")
                .navigationTitle("Awards")
        }
    }
}
