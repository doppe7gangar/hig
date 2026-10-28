import SwiftUI

@main
struct LedgerApp: App {
    var body: some Scene {
        WindowGroup { RootView(state: .loaded(Expense.samples)) }
    }
}

struct RootView: View {
    var state: LoadState<[Expense]>

    var body: some View {
        TabView {
            Tab("Expenses", systemImage: "list.bullet") { ExpensesView(state: state) }
            Tab("Budgets", systemImage: "chart.pie") { Text("Budgets") }
            Tab("Settings", systemImage: "gear") { Text("Settings") }
        }
    }
}

enum LoadState<Value> {
    case loading, loaded(Value), failed
}

struct Expense: Identifiable, Hashable {
    let id = UUID()
    var title: String
    var symbol: String
    var amount: Decimal

    static let samples = [
        Expense(title: "Lunch at Kiln", symbol: "fork.knife", amount: 18.40),
        Expense(title: "Monthly tram pass", symbol: "tram.fill", amount: 42),
        Expense(title: "Groceries", symbol: "cart.fill", amount: 63.15),
    ]
}

struct ExpensesView: View {
    var state: LoadState<[Expense]>
    @State private var period = Period.month
    @State private var adding = false

    enum Period: String, CaseIterable {
        case week = "Week", month = "Month"
    }

    var body: some View {
        NavigationStack {
            content
                .navigationTitle("Expenses")
                .navigationDestination(for: Expense.self) { ExpenseDetailView(expense: $0) }
                .toolbar {
                    ToolbarItem(placement: .topBarTrailing) {
                        Button("Add Expense", systemImage: "plus") { adding = true }
                    }
                }
                .sheet(isPresented: $adding) { AddExpenseView() }
        }
    }

    @ViewBuilder private var content: some View {
        switch state {
        case .loading:
            ProgressView()
        case .loaded(let expenses) where expenses.isEmpty:
            ContentUnavailableView {
                Label("No expenses yet", systemImage: "tray")
            } description: {
                Text("Everything you spend shows up here.")
            } actions: {
                Button("Add Expense") { adding = true }
                    .buttonStyle(.borderedProminent)
            }
        case .loaded(let expenses):
            List {
                Picker("Period", selection: $period) {
                    ForEach(Period.allCases, id: \.self) { Text($0.rawValue) }
                }
                .pickerStyle(.segmented)
                .listRowBackground(Color.clear)

                Section {
                    ForEach(expenses) { expense in
                        NavigationLink(value: expense) {
                            LabeledContent {
                                Text(expense.amount, format: .currency(code: "GBP"))
                            } label: {
                                Label(expense.title, systemImage: expense.symbol)
                            }
                        }
                    }
                }
            }
            .listStyle(.insetGrouped)
        case .failed:
            ContentUnavailableView {
                Label("Couldn’t load expenses", systemImage: "exclamationmark.triangle")
            } description: {
                Text("Check your connection and try again.")
            } actions: {
                Button("Try Again") { }
                    .buttonStyle(.borderedProminent)
            }
        }
    }
}

struct ExpenseDetailView: View {
    let expense: Expense
    @State private var confirmingDelete = false

    var body: some View {
        List {
            LabeledContent("Amount") {
                Text(expense.amount, format: .currency(code: "GBP"))
            }
            Section {
                ShareLink(item: expense.title)
                Button("Delete Expense", role: .destructive) { confirmingDelete = true }
            }
        }
        .navigationTitle(expense.title)
        .confirmationDialog("Delete this expense?", isPresented: $confirmingDelete,
                            titleVisibility: .visible) {
            Button("Delete Expense", role: .destructive) { }
        } message: {
            Text("This can’t be undone.")
        }
    }
}

struct AddExpenseView: View {
    @Environment(\.dismiss) private var dismiss
    @State private var title = ""
    @State private var amount = ""
    @State private var split = false

    var body: some View {
        NavigationStack {
            Form {
                TextField("Description", text: $title)
                TextField("Amount", text: $amount)
                    .keyboardType(.decimalPad)
                Toggle("Split with others", isOn: $split)
            }
            .navigationTitle("New Expense")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel", systemImage: "xmark") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Add", systemImage: "checkmark") { dismiss() }
                }
            }
        }
        .presentationDetents([.medium, .large])
    }
}

#Preview("Populated") { RootView(state: .loaded(Expense.samples)) }
#Preview("Loading") { RootView(state: .loading) }
#Preview("Empty") { RootView(state: .loaded([])) }
#Preview("Error") { RootView(state: .failed) }
