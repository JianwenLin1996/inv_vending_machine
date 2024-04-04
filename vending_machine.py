class VendingMachine:
    def __init__(self):
        self.drink_options = [
            ("Milo",3),
            ("Nescafe",4),
            ("FarmFresh Milk",2)
        ]
        self.note_values = [50, 20, 10, 5, 1]
        self.selected_drinks = []
        self.sum = 0
        self.change = []
        self.change_str = ""
    
    def show_drinks(self):
        print("Available drinks:")
        for index, drink in enumerate(self.drink_options):
            print(f"{index+1} - {drink[0]} (MYR {drink[1]})")
    
    def select_drinks(self):
        try:
            selected_index = int(input("Enter drink number to select, 0 to move next step.\n"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return False

        while True:
            try:                
                if selected_index == 0:
                    return True
                elif 1 <= selected_index <= len(self.drink_options):
                    drink = self.drink_options[selected_index-1]
                    self.selected_drinks.append(drink)
                    self.show_drinks()
                    selected_index = int(input("Choose more?\n"))
                    continue
                else:
                    print("Invalid input.")
                    return False
            except ValueError:
                print("Invalid input. Please enter a number.")
                return False
    
    def show_selected_drinks(self):
        print("You have selected")
        for drink in self.selected_drinks:
            print(drink[0])
            self.sum += drink[1]
        print(f"Total sum is: MYR {self.sum}")

        try:
            pay = int(input("You pay (please enter number)"))
            while True:
                if pay < self.sum:
                    pay = int(input("Insufficient payment, please re-enter"))
                    continue
                else:
                    # process change
                    transaction_change = pay - self.sum
                    if transaction_change == 0:
                        break
                    for note in self.note_values:
                        note_amount = transaction_change // note
                        transaction_change = transaction_change % note
                        self.change.append((note, note_amount))
                        if (transaction_change == 0):
                            break
                break

        except ValueError:
            print("Invalid input. Please enter a number.")
            return False
        
    def show_change(self):
        if len(self.change) > 0:
            for c in self.change:
                self.change_str += f" {c[1]} piece(s) of MYR {c[0]}\n"
            print(f"You received \n{self.change_str} as change")
        print("Thank you. Have a nice day.")

    
    def main(self):
        self.show_drinks()
        while True:
            if self.select_drinks():
                break
            else:
                print("error")
                break
        self.show_selected_drinks()
        self.show_change()

if __name__ == "__main__":
    machine = VendingMachine()
    machine.main()

