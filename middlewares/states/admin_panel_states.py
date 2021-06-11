from aiogram.dispatcher.filters.state import StatesGroup, State



class write_user(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()
    step6 = State()



class remove_user(StatesGroup):
    step1 = State()



class check_user(StatesGroup):
    step1 = State()



class all_info(StatesGroup):
    step1 = State()