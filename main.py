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
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
