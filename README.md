simple_i18n is a minimalist translation tool.
Copyright jmimu 2014 (jmimu@free.fr)

It currently works only for javascript, but it is very easy to adapt it to
an other language.

Add "js_functions.txt" content to your javascript source file.
Change all the immediat strings you want to translate this way:
"example" into _("example").

Then run "prep_translation.py" with 2 parameters:
 - file to translate
 - language short name

Example :
  ./prep_translation.py ex_javascript.html fr

This command will :
 - search for existing translations in selected language
 - search for new words to translate
 - display the new dictionnary, recording all previous translations completed
 with the new words and a default translation (the original word between "~")

You just have to copy that in your source file and correct the tranlations.
Then update the translations list it you added a new language, and set
the language you want as current one.

See the example in ex/js/.
