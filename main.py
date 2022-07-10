from booking.booking import Booking

try:
    with Booking() as bot:
        place = str(input("Where do you wanna go ? "))
        check_in = str(input("Write your check-in date in the following format \'yyyy-mm-dd\' : "))
        check_out = str(input("Write your check-out date in the following format \'yyyy-mm-dd\' : "))
        nbr_ppl = int(input("How many adults are going ? "))
        bot.land_first_page()
        bot.searchplace(place)
        bot.choosedates(check_in,check_out)
        bot.choose_nbr(nbr_ppl)
        bot.search()
        bot.closepop()
        bot.apply_filtre()
        bot.refresh()
        bot.closepop()
        nom_fichier = f"Hotels in {place} from {check_in} to {check_in}"
        bot.report_results(nom_fichier)
except Exception as E:
    if "in PATH" in str(E):
        print('We can\'t get this program to run from the terminal.\nAdd the chrome driver to the PATH system variable.')
    else:
        raise
