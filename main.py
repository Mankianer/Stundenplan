import stundenplan


# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    slotmap = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 10: 1}
    slotmap2 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    wochentage = [stundenplan.classes.Wochentag("Montag", slotmap),
                  stundenplan.classes.Wochentag("Dienstag", slotmap),
                  stundenplan.classes.Wochentag("Mittwoch", slotmap2),
                  stundenplan.classes.Wochentag("Donnerstag", slotmap),
                  stundenplan.classes.Wochentag("Freitag", slotmap)]

    fächer = [stundenplan.classes.Fach("Mathe", 6), stundenplan.classes.Fach("Deutsch", 6)]

    stundenplan = stundenplan.classes.Stundenplan(klassenstufe=10, fächer=fächer, wochentage=wochentage)

    print(stundenplan.get_as_table())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
