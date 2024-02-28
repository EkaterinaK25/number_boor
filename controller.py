import view
from model import PhoneBook
import text


# def find_contacts(phone_book, message):
#     search_word = view.input_data(text.message)
#     result = phone_book.find_contact(search_word)
#     view.show_contacts(result, text.find_contact_no_result(search_word))
#     return True if result else False

def srtart_app():
    pb = PhoneBook()
    while True:
        user_choice = view.show_main_menu()
        match user_choice:
            case 1:
                pb.open_phone_book()
                view.show_message(text.phone_book_opened_successful)
            case 2:
                pb.save_phone_book()
                view.show_message(text.phone_book_saved_successful)
            case 3:
                view.show_contacts(pb.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = view.input_data(text.input_new_contact)
                pb.add_new_contact(new_contact)
                view.show_message(text.new_contact_added_successful)
            case 5:
                pb.find_contacts(view.input_data, view.show_contacts, text.input_search_word, text.find_contscts_no_results)
            case 6:
                if pb.find_contacts(view.input_data, view.show_contacts, text.input_search_word_for_edit, text.find_contscts_no_results):
                    u_id = int(view.input_data(text.input_id_for_edit))
                    edited_contact = view.input_data(text.edit_contact)
                    name = pb.edit_contact(u_id, edited_contact)
                    view.show_message(text.edit_contact_successful(name))
            case 7:
                if pb.find_contacts(view.input_data, view.show_contacts, text.input_search_word_for_delete, text.find_contscts_no_results):
                    u_id = int(view.input_data(text.input_id_for_delete))
                    name = pb.delete_contact(u_id)
                    view.show_message(text.edit_contact_successful(name))
            case 8:
                if pb.on_exit():
                    view.show_message(text.exit_changes)
                    if view.input_data(text.exit_confirm).lower() == 'y':
                        pb.save_phone_book()
                        view.show_message(text.exit_no_changes_confirm)
                    else:
                        view.show_message(text.exit_no_changes_no_confirm)

                
                else:
                    view.show_message(text.exit_no_changes)
                break
