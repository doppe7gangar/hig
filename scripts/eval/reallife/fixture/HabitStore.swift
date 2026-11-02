import SwiftUI

struct Habit: Identifiable, Equatable {
    let id = UUID()
    var name: String
    var subtitle: String
    var isDoneToday: Bool = false
    var completedCount: Int = 0
    var streak: Int = 0
    var chartColor: Color = .blue
}

@MainActor
final class HabitStore: ObservableObject {
    @Published var habits: [Habit] = [
        Habit(name: "Morning run", subtitle: "3 km", isDoneToday: true,
              completedCount: 12, streak: 4, chartColor: .green),
        Habit(name: "Read", subtitle: "20 minutes",
              completedCount: 30, streak: 9, chartColor: .orange),
        Habit(name: "Water", subtitle: "8 glasses",
              completedCount: 5, streak: 1, chartColor: .red),
    ]

    @Published var remindersOn = true
    @Published var hideCompleted = false

    func toggle(_ habit: Habit) {
        guard let i = habits.firstIndex(of: habit) else { return }
        habits[i].isDoneToday.toggle()
        habits[i].completedCount += habits[i].isDoneToday ? 1 : -1
    }

    func add(name: String, subtitle: String) {
        habits.append(Habit(name: name, subtitle: subtitle))
    }

    func delete(_ habit: Habit) {
        habits.removeAll { $0 == habit }
    }

    func resetAll() {
        habits.removeAll()
    }
}
