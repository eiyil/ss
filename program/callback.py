# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبآ عزيزي ‹[{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) ›**\n
 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) **
** ‹ يمكنك من خلال هذا البوت تشغيل الاغاني و الفيديوهات في مجموعتك › **
 ** ‹ يمكنك اكتشاف الاوامر من خلال الزر في الاسفل › **
 ** ‹ يمكنك معرفة كيفية استخدام البوت من خلال الزر في الاسفل › **
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اضفني الى مجموعتك ›",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("‹ دليل الاستخدام ›", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("‹ الاوامر ›", callback_data="cbbasic"),
                    InlineKeyboardButton("‹ المطور ›", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "‹ مجموعة الدعم ›", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "‹ قناة السورس ›", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" الدليل الأساسي لاستخدام هذا البوت:

 1 - أولاً ، أضفني إلى مجموعتك
 2 - بعد ذلك ، قم بترقيتي كمشرف ومنح جميع الصلاحيات باستثناء الوضع الخفي
 3 - بعد ترقيتي ، اكتب /reload مجموعة لتحديث بيانات المشرفين
 3 - أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب /userbotjoin لدعوة حساب المساعد
 4 - قم بتشغيل المكالمة  أولاً قبل البدء في تشغيل الفيديو / الموسيقى
 5 - في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر /reload في إصلاح بعض المشكلات
   إذا لم ينضم البوت إلى المكالمة ، فتأكد من تشغيل المكالمة  بالفعل ، أو اكتب /userbotleave ثم اكتب /userbotjoin مرة أخرى

 ‹ سورس مالوركا ›
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" ها هي الأوامر الأساسية:
 - /mplay 「اسم الأغنية / رابط」تشغيل الصوت mp3
 - /vplay 「اسم / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
- /stream 「رابط 」تشغيل صوت
- /vstream 「رابط」 تشغيل بث مباشر من اليوتيوب
- /stop لايقاف التشغيل
- /resume استئناف التشغيل
- /skip تخطي الئ التالي
- /pause ايقاف التشغيل موقتآ
- /vmute لكتم البوت
- /vunmute لرفع الكتم عن البوت
‹ سورس مالوركا ›""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ التالي ›", callback_data="cbadmin")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""- /playlist ↤ تظهر لك قائمة التشغيل
- /video + الاسم  تنزيل فيديو من youtube
- /song + الاسم تنزيل صوت من youtube
- /volume + الرقم لضبط مستوئ الصوت
- /reload لتحديث البوت و قائمة المشرفين
- /userbotjoin لاستدعاء حساب المساعد
- /userbotleave لطرد حساب المساعد 
 - /ping - إظهار حالة البوت بينغ
 - /alive  إظهار معلومات البوت  (في المجموعة)
 ‹ سورس مالوركا ›""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("‹ رجوع ›", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

 __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("الامر ليس لك او انك لا تملك صلاحية ادارة الدردشة الصوتية", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇: كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("‹ اغلاق ›", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("‹ قائمة التشغيل فارغة ›", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("الامر ليس لك او انك لا تملك صلاحية ادارة الدردشة الصوتية", show_alert=True)
    await query.message.delete()
