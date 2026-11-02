import SwiftUI

struct ContentView: View {
    @StateObject private var store = HabitStore()

    var body: some View {
        TabView {
            TodayView(store: store)
                .tabItem { Label("Today", systemImage: "checkmark.circle") }

            HistoryView(store: store)
                .tabItem { Label("History", systemImage: "calendar") }

            StatsView(store: store)
                .tabItem { Label("Stats", systemImage: "chart.bar") }

            StreaksView(store: store)
                .tabItem { Label("Streaks", systemImage: "flame") }

            RemindersView(store: store)
                .tabItem { Label("Reminders", systemImage: "bell") }

            AchievementsView(store: store)
                .tabItem { Label("Awards", systemImage: "rosette") }

            SettingsView(store: store)
                .tabItem { Label("Settings", systemImage: "gear") }
        }
        .accentColor(.purple)
    }
}

struct TodayView: View {
    @ObservedObject var store: HabitStore
    @State private var showingAddSheet = false
    @State private var habitPendingDelete: Habit?
    @State private var showingCustomEditor = false

    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVStack(spacing: 12) {
                    ForEach(store.habits) { habit in
                        HabitRow(habit: habit, store: store) {
                            habitPendingDelete = habit
                        }
                    }
                }
                .padding()
            }
            .background(Color.white)
            .navigationTitle("Today")
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button {
                        showingAddSheet = true
                    } label: {
                        Image(systemName: "plus")
                            .frame(width: 30, height: 30)
                    }
                }
                ToolbarItem(placement: .topBarLeading) {
                    Button {
                        showingCustomEditor = true
                    } label: {
                        Image(systemName: "slider.horizontal.3")
                            .frame(width: 30, height: 30)
                    }
                }
            }
            .sheet(isPresented: $showingAddSheet) {
                AddHabitView(store: store)
            }
            .alert("Delete Habit?", isPresented: .constant(habitPendingDelete != nil)) {
                Button("Cancel", role: .cancel) { habitPendingDelete = nil }
                Button("Delete") {
                    if let h = habitPendingDelete { store.delete(h) }
                    habitPendingDelete = nil
                }
            } message: {
                Text("This will remove the habit from today's list.")
            }
            .overlay {
                if showingCustomEditor {
                    ZStack {
                        Color.black.opacity(0.4)
                            .ignoresSafeArea()
                            .onTapGesture { showingCustomEditor = false }
                        VStack(spacing: 16) {
                            Text("Quick Filters")
                                .font(.system(size: 20, weight: .bold))
                            Toggle("Hide completed", isOn: $store.hideCompleted)
                            Button("Done") { showingCustomEditor = false }
                        }
                        .padding(24)
                        .background(Color.white)
                        .cornerRadius(14)
                        .padding(40)
                    }
                }
            }
        }
    }
}

struct HabitRow: View {
    let habit: Habit
    @ObservedObject var store: HabitStore
    var onDelete: () -> Void

    var body: some View {
        HStack(spacing: 12) {
            Circle()
                .fill(habit.isDoneToday ? Color.green : Color.red)
                .frame(width: 10, height: 10)

            VStack(alignment: .leading, spacing: 2) {
                Text(habit.name)
                    .font(.system(size: 15))
                    .foregroundColor(.black)
                Text(habit.subtitle)
                    .font(.system(size: 12))
                    .foregroundColor(Color(white: 0.55))
            }

            Spacer()

            Button {
                store.toggle(habit)
            } label: {
                Image(systemName: habit.isDoneToday ? "checkmark.circle.fill" : "circle")
                    .font(.title2)
                    .frame(width: 44, height: 44)
            }

            Button {
                onDelete()
            } label: {
                Image(systemName: "trash")
                    .frame(width: 28, height: 28)
            }
        }
        .padding(12)
        .background(Color.white)
        .cornerRadius(10)
    }
}
