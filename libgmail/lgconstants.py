#
# Generated file -- DO NOT EDIT
#
# Note: This file is now edited! 2005-04-25
#
# constants.py -- Useful constants extracted from Gmail Javascript code
#
# Source version: 44f09303f2d4f76f
#
# Generated: 2004-08-10 13:08 UTC
#


URL_LOGIN = "https://www.google.com/accounts/ServiceLoginBoxAuth"
URL_GMAIL = "https://mail.google.com/mail/"


# Constants with names not from the Gmail Javascript:
U_SAVEDRAFT_VIEW = "sd"

D_DRAFTINFO = "di"
# NOTE: All other DI_* field offsets seem to match the MI_* field offsets
DI_BODY = 19

versionWarned = False # If the Javascript version is different have we
                      # warned about it?


js_version = '44f09303f2d4f76f'

D_VERSION = "v"
D_QUOTA = "qu"
D_DEFAULTSEARCH_SUMMARY = "ds"
D_THREADLIST_SUMMARY = "ts"
D_THREADLIST_END = "te"
D_THREAD = "t"
D_CONV_SUMMARY = "cs"
D_CONV_END = "ce"
D_MSGINFO = "mi"
D_MSGBODY = "mb"
D_MSGATT = "ma"
D_COMPOSE = "c"
D_CONTACT = "co"
D_CATEGORIES = "ct"
D_CATEGORIES_COUNT_ALL = "cta"
D_ACTION_RESULT = "ar"
D_SENDMAIL_RESULT = "sr"
D_PREFERENCES = "p"
D_PREFERENCES_PANEL = "pp"
D_FILTERS = "fi"
D_GAIA_NAME = "gn"
D_INVITE_STATUS = "i"
D_END_PAGE = "e"
D_LOADING = "l"
D_LOADED_SUCCESS = "ld"
D_LOADED_ERROR = "le"
D_QUICKLOADED = "ql"
QU_SPACEUSED = 0
QU_QUOTA = 1
QU_PERCENT = 2
QU_COLOR = 3
TS_START = 0
TS_NUM = 1
TS_TOTAL = 2
TS_ESTIMATES = 3
TS_TITLE = 4
TS_TIMESTAMP = 5 + 1
TS_TOTAL_MSGS = 6 + 1
T_THREADID = 0
T_UNREAD = 1
T_STAR = 2
T_DATE_HTML = 3
T_AUTHORS_HTML = 4
T_FLAGS = 5
T_SUBJECT_HTML = 6
T_SNIPPET_HTML = 7
T_CATEGORIES = 8
T_ATTACH_HTML = 9
T_MATCHING_MSGID = 10
T_EXTRA_SNIPPET = 11
CS_THREADID = 0
CS_SUBJECT = 1
CS_TITLE_HTML = 2
CS_SUMMARY_HTML = 3
CS_CATEGORIES = 4
CS_PREVNEXTTHREADIDS = 5
CS_THREAD_UPDATED = 6
CS_NUM_MSGS = 7
CS_ADKEY = 8
CS_MATCHING_MSGID = 9
MI_FLAGS = 0
MI_NUM = 1
MI_MSGID = 2
MI_STAR = 3
MI_REFMSG = 4
MI_AUTHORNAME = 5
MI_AUTHORFIRSTNAME = 6 # ? -- Name supplied by rj
MI_AUTHOREMAIL = 6 + 1
MI_MINIHDRHTML = 7 + 1
MI_DATEHTML = 8 + 1
MI_TO = 9 + 1
MI_CC = 10 + 1
MI_BCC = 11 + 1
MI_REPLYTO = 12 + 1
MI_DATE = 13 + 1
MI_SUBJECT = 14 + 1
MI_SNIPPETHTML = 15 + 1
MI_ATTACHINFO = 16 + 1
MI_KNOWNAUTHOR = 17 + 1
MI_PHISHWARNING = 18 + 1
A_ID = 0
A_FILENAME = 1
A_MIMETYPE = 2
A_FILESIZE = 3
CT_NAME = 0
CT_COUNT = 1
AR_SUCCESS = 0
AR_MSG = 1
SM_COMPOSEID = 0
SM_SUCCESS = 1
SM_MSG = 2
SM_NEWTHREADID = 3
CMD_SEARCH = "SEARCH"
ACTION_TOKEN_COOKIE = "GMAIL_AT"
U_VIEW = "view"
U_PAGE_VIEW = "page"
U_THREADLIST_VIEW = "tl"
U_CONVERSATION_VIEW = "cv"
U_COMPOSE_VIEW = "cm"
U_PRINT_VIEW = "pt"
U_PREFERENCES_VIEW = "pr"
U_JSREPORT_VIEW = "jr"
U_UPDATE_VIEW = "up"
U_SENDMAIL_VIEW = "sm"
U_AD_VIEW = "ad"
U_REPORT_BAD_RELATED_INFO_VIEW = "rbri"
U_ADDRESS_VIEW = "address"
U_ADDRESS_IMPORT_VIEW = "ai"
U_SPELLCHECK_VIEW = "sc"
U_INVITE_VIEW = "invite"
U_ORIGINAL_MESSAGE_VIEW = "om"
U_ATTACHMENT_VIEW = "att"
U_DEBUG_ADS_RESPONSE_VIEW = "da"
U_SEARCH = "search"
U_INBOX_SEARCH = "inbox"
U_STARRED_SEARCH = "starred"
U_ALL_SEARCH = "all"
U_DRAFTS_SEARCH = "drafts"
U_SENT_SEARCH = "sent"
U_SPAM_SEARCH = "spam"
U_TRASH_SEARCH = "trash"
U_QUERY_SEARCH = "query"
U_ADVANCED_SEARCH = "adv"
U_CREATEFILTER_SEARCH = "cf"
U_CATEGORY_SEARCH = "cat"
U_AS_FROM = "as_from"
U_AS_TO = "as_to"
U_AS_SUBJECT = "as_subj"
U_AS_SUBSET = "as_subset"
U_AS_HAS = "as_has"
U_AS_HASNOT = "as_hasnot"
U_AS_ATTACH = "as_attach"
U_AS_WITHIN = "as_within"
U_AS_DATE = "as_date"
U_AS_SUBSET_ALL = "all"
U_AS_SUBSET_INBOX = "inbox"
U_AS_SUBSET_STARRED = "starred"
U_AS_SUBSET_SENT = "sent"
U_AS_SUBSET_DRAFTS = "drafts"
U_AS_SUBSET_SPAM = "spam"
U_AS_SUBSET_TRASH = "trash"
U_AS_SUBSET_ALLSPAMTRASH = "ast"
U_AS_SUBSET_READ = "read"
U_AS_SUBSET_UNREAD = "unread"
U_AS_SUBSET_CATEGORY_PREFIX = "cat_"
U_THREAD = "th"
U_PREV_THREAD = "prev"
U_NEXT_THREAD = "next"
U_DRAFT_MSG = "draft"
U_START = "start"
U_ACTION = "act"
U_ACTION_TOKEN = "at"
U_INBOX_ACTION = "ib"
U_MARKREAD_ACTION = "rd"
U_MARKUNREAD_ACTION = "ur"
U_MARKSPAM_ACTION = "sp"
U_UNMARKSPAM_ACTION = "us"
U_MARKTRASH_ACTION = "tr"
U_ADDCATEGORY_ACTION = "ac_"
U_REMOVECATEGORY_ACTION = "rc_"
U_ADDSTAR_ACTION = "st"
U_REMOVESTAR_ACTION = "xst"
U_ADDSENDERTOCONTACTS_ACTION = "astc"
U_DELETEMESSAGE_ACTION = "dm"
U_DELETE_ACTION = "dl"
U_EMPTYSPAM_ACTION = "es_"
U_EMPTYTRASH_ACTION = "et_"
U_SAVEPREFS_ACTION = "prefs"
U_ADDRESS_ACTION = "a"
U_CREATECATEGORY_ACTION = "cc_"
U_DELETECATEGORY_ACTION = "dc_"
U_RENAMECATEGORY_ACTION = "nc_"
U_CREATEFILTER_ACTION = "cf"
U_REPLACEFILTER_ACTION = "rf"
U_DELETEFILTER_ACTION = "df_"
U_ACTION_THREAD = "t"
U_ACTION_MESSAGE = "m"
U_ACTION_PREF_PREFIX = "p_"
U_REFERENCED_MSG = "rm"
U_COMPOSEID = "cmid"
U_COMPOSE_MODE = "cmode"
U_COMPOSE_SUBJECT = "su"
U_COMPOSE_TO = "to"
U_COMPOSE_CC = "cc"
U_COMPOSE_BCC = "bcc"
U_COMPOSE_BODY = "body"
U_PRINT_THREAD = "pth"
CONV_VIEW = "conv"
TLIST_VIEW = "tlist"
PREFS_VIEW = "prefs"
HIST_VIEW = "hist"
COMPOSE_VIEW = "comp"
HIDDEN_ACTION = 0
USER_ACTION = 1
BACKSPACE_ACTION = 2

# TODO: Get these on the fly?
STANDARD_FOLDERS = [U_INBOX_SEARCH, U_STARRED_SEARCH,
                    U_ALL_SEARCH, U_DRAFTS_SEARCH,
                    U_SENT_SEARCH, U_SPAM_SEARCH]

