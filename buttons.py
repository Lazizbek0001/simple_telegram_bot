from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "O'zbekcha", callback_data='uz'),
            InlineKeyboardButton(text= "English", callback_data='en')
        ]
    ]
)



uzbek = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Loyiha haqida", callback_data='loyiha'),
            InlineKeyboardButton(text= "Ro'yhatdan o'tish", callback_data= 'register')
        ],
        [
            InlineKeyboardButton(text = "Savollar yo'llash", callback_data="savol")
        ]
    ]
)

english = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "About the project", callback_data='project'),
            InlineKeyboardButton(text= "Registration", callback_data= 'register1')
        ],
        [
            InlineKeyboardButton(text = "Send questions", callback_data="question")
        ]
    ]
)


project = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Aim of the project", callback_data="aim"),
            InlineKeyboardButton(text="Project task", callback_data="task")
        ],
        [
            InlineKeyboardButton(text= "The order of proccess", callback_data='order'),
            InlineKeyboardButton(text= "Requirements", callback_data="demand")
        ],
        [
            InlineKeyboardButton(text= "Back", callback_data="back8")
        ]
    ]
)


Aim = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Back", callback_data="back9")
        ]
    ]
)

task = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Back", callback_data="back10")
        ]
    ]
)

order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Back", callback_data="back11")
        ]
    ]
)

demand = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Back", callback_data="back12")
        ]
    ]
)


register = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Back", callback_data="back13")
        ]
    ]
)


question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Back", callback_data="back14")
        ]
    ]
)



loyiha = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Loyiha maqsadi", callback_data="maqsad"),
            InlineKeyboardButton(text="Loyiha vazifasi", callback_data="vazifa")
        ],
        [
            InlineKeyboardButton(text= "O'tkazilish tartibi", callback_data='tartib'),
            InlineKeyboardButton(text= "Talablar", callback_data="talab")

        ],
        [
            InlineKeyboardButton(text= "Orqaga", callback_data="back1")
        ]
    ]
)

maqsad = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Orqaga", callback_data="back2")
        ]
    ]
)

vazifa = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Orqaga", callback_data="back3")
        ]
    ]
)

tartib = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Orqaga", callback_data="back4")
        ]
    ]
)

talab = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Orqaga", callback_data="back5")
        ]
    ]
)

royhat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Orqaga", callback_data="back6")
        ]
    ]
)


savol = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text= "Orqaga", callback_data="back7")
        ]
    ]
)