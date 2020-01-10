Name:       ibus-typing-booster
Version:    1.2.3
Release:    5%{?dist}
Summary:    A typing booster engine for the IBus platform
License:    GPLv3+
Group:      System Environment/Libraries
URL:        http://git.fedorahosted.org/git/?p=ibus-typing-booster.git
Source0:    https://fedorahosted.org/releases/i/b/ibus-typing-booster/%{name}-%{version}.tar.gz
Patch0:     Commit-candidate-clicked-on-with-the-mouse.patch
Patch1:     0001-Call-IBus.Bus-in-__main__-not-in-__init__-of-class-S.patch
Requires:   ibus
Requires:   libtranslit-m17n
BuildRequires:  ibus-devel,libtranslit-devel
Provides:   ibus-hunspell-table = %{version}-%{release}
Obsoletes:  ibus-hunspell-table <= 0.0.6-1.fc17
Provides:   ibus-hunspell-table = %{version}-%{release}
Obsoletes:  ibus-hunspell-table <= 0.0.8-2.fc18
Provides:   ibus-indic-table = %{version}-%{release}
Obsoletes:  ibus-indic-table <= 1.3.1-23.fc17
Provides:   ibus-european-table = %{version}-%{release}
Obsoletes:  ibus-european-table <= 1.1.6-1.fc17
Provides:   ibus-european-table = %{version}-%{release}
Obsoletes:  ibus-european-table <= 1.1.6-2.fc18
Provides:   english-typing-booster = %{version}-%{release}
Obsoletes:  english-typing-booster <= 0.0.2-1.fc17
Provides:   english-typing-booster = %{version}-%{release}
Obsoletes:  english-typing-booster <= 0.0.2-2.fc18
Provides:   bengali-typing-booster-inscript = %{version}-%{release}
Obsoletes:  bengali-typing-booster-inscript <= 0.9.0-2.fc17
Provides:   bengali-typing-booster-phonetic = %{version}-%{release}
Obsoletes:  bengali-typing-booster-phonetic <= 0.9.0-2.fc17
Provides:   bengali-typing-booster-probhat = %{version}-%{release}
Obsoletes:  bengali-typing-booster-probhat <= 0.9.0-2.fc17
Provides:   gujarati-typing-booster-inscript = %{version}-%{release}
Obsoletes:  gujarati-typing-booster-inscript <= 0.9.0-3.fc17
Provides:   gujarati-typing-booster-phonetic = %{version}-%{release}
Obsoletes:  gujarati-typing-booster-phonetic <= 0.9.0-3.fc17
Provides:   hindi-typing-booster-phonetic = %{version}-%{release}
Obsoletes:  hindi-typing-booster-phonetic <= 0.9.0-2.fc17
Provides:   hindi-typing-booster-inscript = %{version}-%{release}
Obsoletes:  hindi-typing-booster-inscript <= 0.9.0-2.fc17
Provides:   marathi-typing-booster-inscript = %{version}-%{release}
Obsoletes:  marathi-typing-booster-inscript <= 0.9.0-2.fc17
Provides:   marathi-typing-booster-phonetic = %{version}-%{release}
Obsoletes:  marathi-typing-booster-phonetic <= 0.9.0-2.fc17
Provides:   tamil-typing-booster-inscript = %{version}-%{release}
Obsoletes:  tamil-typing-booster-inscript <= 0.9.0-2.fc17
Provides:   tamil-typing-booster-99 = %{version}-%{release}
Obsoletes:  tamil-typing-booster-99 <= 0.9.0-2.fc17

BuildArch:  noarch

%description
The Typing Booster engine for IBus platform.

%prep
%setup -q
%patch0 -p2 -b .Commit-candidate-clicked-on-with-the-mouse
%patch1 -p2 -b .0001-Call-IBus.Bus-in-__main__-not-in-__init__-of-class-S

%build
%configure --disable-static --disable-additional
make %{?_smp_mflags}

%install 
make install DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true  INSTALL="install -p"   pkgconfigdir=%{_datadir}/pkgconfig

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README 
%{_datadir}/%{name}
%{_datadir}/ibus/component/typing-booster.xml
%{_libexecdir}/ibus-engine-typing-booster
%{_libexecdir}/ibus-setup-typing-booster
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/applications/ibus-setup-typing-booster.desktop

%changelog
* Mon May 22 2017 Mike FABIAN <mfabian@redhat.com> - 1.2.3-5
- Call IBus.Bus() in __main__, not in __init__ of class SetupUI
- Resolves: rhbz#1447332

* Fri Jan 10 2014 Mike FABIAN <mfabian@redhat.com> - 1.2.3-4
- Commit candidate clicked on with the mouse (Related: rhbz#1038521)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.3-3
- Mass rebuild 2013-12-27

* Tue Aug 06 2013 Mike FABIAN <mfabian@redhat.com> - 1.2.3-1
- Update to 1.2.3 upstream version
- Fix exception handling when trying to install a rpm package (Resolves: rhbz#986178)

* Mon Jul 15 2013 Mike FABIAN <mfabian@redhat.com> - 1.2.2-1
- Update to 1.2.2 upstream version
- Commit immediately when certain punctuation characters are typed and transliteration is not used (Resolves: rhbz#981179)
- Add an option to try completion only when a minimum number of characters has been typed

* Wed Jul 03 2013 Mike FABIAN <mfabian@redhat.com> - 1.2.1-1
- Update to 1.2.1 upstream version
- Pop up a message box when a file has been read to train the database, indicating success or failure (Resolves: rhbz#979933)
- Update German translation
- Ignore most punctuation characters and mathematical symbols when tokenizing (Resolves: rhbz#979939)

* Fri Jun 28 2013 Mike FABIAN <mfabian@redhat.com> - 1.2.0-1
- Update to 1.2.0 upstream version
- Make TAB when used to enable/disable the lookup table work as a toogle
- Create a VIEW for “LIKE input_phrase%” in select_words() and use that
  in the following SELECT statements (Makes candidate calculation more
  than 10 times faster)

* Mon Jun 24 2013 Mike FABIAN <mfabian@redhat.com> - 1.1.0-1
- Update to 1.1.0 upstream version
- Add a commit=True parameter to check_phrase_and_update_frequency()
- Fix that the page_size is shown as 0 in the setup tool if it has not been set before
- Do not use AUTOINCREMENT
- Make it possible to exit the setup tool by typing Control-C in the terminal
- Add feature to read a text file for training the user database
- Update German translations and .pot file
- Fix error when the hunspell dictionary for an engine is missing

* Tue Jun 18 2013 Mike FABIAN <mfabian@redhat.com> - 1.0.3-1
- Update to 1.0.3 upstream version
- Don’t output page_size in “/usr/libexec/ibus-engine-typing-booster --xml” (Resolves: rhbz#975449 - ibus-daemon prints warnings because “/usr/libexec/ibus-engine-typing-booster --xml” prints the invalid element “page_size”)
- Use ~/.local/share/ibus-typing-booster/ to store user data and log files (Resolves: rhbz#949035 - don't use a hidden directory under .local/share)

* Fri Jun 14 2013 Mike FABIAN <mfabian@redhat.com> - 1.0.2-1
- Update to 1.0.2 upstream version
- Push context *after* writing the trigram to the database

* Fri Jun 14 2013 Mike FABIAN <mfabian@redhat.com> - 1.0.1-1
- Update to 1.0.1 upstream version
- Fix problem when IBUS_TYPING_BOOSTER_DEBUG_LEVEL is not set

* Thu Jun 13 2013 Mike FABIAN <mfabian@redhat.com> - 1.0.0-1
- Update to 1.0.0 upstream version
- Remove mudb and use “Write-Ahead Logging”
- Introduce an environment variable IBUS_TYPING_BOOSTER_DEBUG_LEVEL for debugging
- Speed up converting an old database to the current format
- Make prediction more intelligent by using context of up to 2 previous words
- Automatically remove whitespace between the last word and a punctuation character ending a sentence

* Sun Jun 02 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.32-1
- Update to 0.0.32 upstream version
- Resolves: rhbz#969847 - Editing in the preëdit of ibus-typing-booster behaves weird, especially with transliteration
- Fix behaviour of Control+Number
- When committing by typing TAB, update frequency data in user database
- When committing by tying RETURN or ENTER, update frequency data in user database
- Do not try to match very long words in the hunspell dictionaries
- Rewrite the code for moving and editing within the preëdit (rhbz#969847)
- Fix encoding error when changing values with the setup tool
- Add ko_KR.conf and ko_KR.svg
- Use normalization forms NFD or NFKD internally and NFC externally
- Remove old way of using libtranslit via ctypes
- Get rid of “freq” column in databases
- Remove too simpleminded auto-capitalization

* Wed May 29 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.31-1
- Update to 0.0.31 upstream version
- Resolves: rhbz#968209 - Typing characters which are not explicitly listed as “valid_input_chars” in .conf files in ibus-typing-booster get inserted in a weird position
- Remove lots of unused and/or useless code
- Simplify some code
- Fix the problem that after “page down” the first “arrow down” does not move down in the lookup table
- Never use “-” or “=” as page up and page down keys
- Print more useful debug output when an exception happens
- Replace unencodable characters when asking pyhunspell for suggestions
- Get dictionary encoding from .aff file
- Get rid of the the variable “valid_input_chars” (rhbz#968209)
- Remove option “valid_input_chars” from .conf files and template.txt
- Replace keysym2unichr(key.code) with IBus.keyval_to_unicode(key.code)

* Sun May 26 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.30-1
- Update to 0.0.30 upstream version
- simplify database structure and code
- The Swedish hunspell dictionary is in UTF-8, not ISO-8859-1
- SQL LIKE should behave case sensitively
- Do not throw away the input phrase in hunspell_suggest.suggest()
- Merge candidates which have the same resulting phrase in select_words()
- Remove phrases always from the user database when typing Alt+Number
- Sync memory user database “mudb” to disk user database “user_db” on focus out
- Delete all records from mudb after syncing to user_db
- Do not prevent phrases of length < 4 to be added to the frequency database
- Resolves: #966947 - When typing a/ with the da_DK ibus-typing-booster, one gets weird matches like a/ACJSTVW
- Do not use lang_chars for matching in the hunspell dictionaries, return immediately if input contains a “/” (Resolves: #966947)
- Remove lang_chars variable
- Use re.escape() to escape the string typed by the user correctly for use in a regular expression
- When removing a phrase with Alt+Number, remove it independent of the input_phrase

* Tue May 14 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.29-1
- Update to 0.0.29 upstream version
- Resolves: #962609  - [abrt] ibus-typing-booster-0.0.28-1.fc19: main.py:107:__init__:AttributeError: tabsqlitedb instance has no attribute 'get_ime_property' (Fix setup tool to use the new class for parsing the config files)
- Avoid adding duplicates to the database by checking first whether phrase is already there in add_phrase()

* Fri May 10 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.28-1
- Update to 0.0.28 upstream version
- Resolves: #961923 - python /usr/share/ibus-typing-booster/engine/main.py --xml is extremely slow when many hunspell dictionaries are installed
- Put the input phrase into a single column in the databases instead of using one column for each character
- Get rid of tab_dict

* Mon May 06 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.27-1
- Update to 0.0.27 upstream version
- Resolves: #959860 - [as_IN] Wrong keymap name Assami (fix spelling error in language name for Assamese)
- Resolves: #958770 - [ibus-typing-Booster][gu-IN]- Typo error (fix spelling error in language name for Gujarati)
- Resolves: #875285 - IME names too long in gnome-shell Input Sources indicator (remove ✓ from symbol in the .conf files)
- simplify code in select_words()
- remove some unused functions

* Thu Feb 14 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.26-1
- Update to 0.0.26 upstream version
- Resolves: #910986 - The arrow icons at the bottom of the candidate lookup table of ibus-typing-booster do not work
- Use different .svg icons for all engines
- Increase number of suggestions from hunspell
- Use the auxiliary text to display the number of candidates
- Make the display of the number of candidates in the auxiliary text optional
- Display of the number of candidates needs to be updated on page-up and page-down

* Thu Feb 14 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.25-1
- Update to 0.0.25 upstream version
- Port to use pygobject3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.24-1
- Update to 0.0.24 upstream version
- Resolves: #884808 - ibus-typing-booster should also show candidates which correct spelling errors
- Use pyhunspell to add spell-checking suggestions
- Use underline for preedit
- Colourize spellchecking suggestions and system phrases already used

* Fri Nov 23 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.23-1
- Update to 0.0.23 upstream version
- Resolves: #879261  dictionary is not automatically reloaded when it is installed via the setup tool
- Make the engine reload the dictionary when the dictionary is installed via the setup tool

* Wed Nov 14 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.22-1
- Update to 0.0.22 upstream version
- Resolves: #876666 Properties of ibus-typing-booster to select input methods are not shown by gnome-shell in f18
- Make the engine use the input method from the dconf setting
- Add combobox to setup GUI to select input method
- Update German translation

* Mon Nov 12 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.21-1
- Update to 0.0.21 upstream version
- Resolves: #875285 Shorten symbol displayed in gnome panel
- Add space before ( in long display name

* Thu Nov 08 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.20-1
- Update to 0.0.20 upstream version
- Resolves: #874421
- Improve setup GUI to make correct dictionary installable (Resolves #874421)
- Add page size spin button to setup tool
- Connect signals in __init__ of SetupUI after setting the initial values
- Make the setup tool find the right config file in gnome-shell on Fedora 18
- Update German translation

* Tue Nov 06 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.19-1
- Update to 0.0.19 upstream version
- fix rpmlint warning “incorrect-fsf-address”

* Wed Oct 31 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.18-1
- Update to 0.0.18 upstream version
- Resolves: #871056
- Save setup option “Enable suggestions by Tab Key” correctly in dconf (Resolves: #871056)
- Make setup dialog translatable and add German translations

* Wed Oct 24 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.16-1
- Update to 0.0.16 upstream version
- Resolves: #869687
- Make enabling the lookup table with the TAB key work correctly
- Simplify code in add_input()
- Make German input typed in NFD work

* Mon Oct 22 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.15-1
- Update to 0.0.15 upstream version
- Resolves: #869050
- Make sure the lookup table is hidden if there are no candidates to suggest (#869050)

* Mon Oct 22 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.14-1
- Update to 0.0.14 upstream version
- Show an obvious warning when the hunspell dictionary needed is not found
- Show exact matches in the .dic files as suggestions as well
- Do not forget the input method used last when activating a previously used engine
- Make spelling of the value of “symbol” in the .conf files more consistent
- include the file ru_RU.conf

* Thu Oct 18 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.13-1
- Update to 0.0.13 upstream version, in 0.0.12 I forgot to
  include the file de_DE.conf

* Thu Oct 18 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.12-1
- Update to 0.0.12 upstream version, in 0.0.11 I forgot to
  include the file keysym2ucs.py

* Thu Oct 18 2012 Mike FABIAN <mfabian@redhat.com> - 0.0.11-1
- Upstream has released 0.0.11 version containing the following
  improvements:
- Add .conf files for many languages and improve some existing .conf files
- Read other_ime option case insensitively
- Split only at the first = in a line in a .conf file
- Fix the problem that the user defined phrases are lost when switching engines
- use “layout = default” instead of “layout = us” in all .conf files
- Make sure the input of transliterate() is UTF-8 encoded
- Add a keysym2unichr() function and use it to support languages which have non Latin1 input
- Let first letter start with index 1 in autogenerated tabdict
- Use autogenerated tabdict always, not only in m17n mode
- Use special value 'NoIme' to indicate that no input method should be used
- Use contents of lang_chars for the regexp to match words in the dictionaries
- In process_key_event, do not return False when a non-ASCII character has been typed
- Read option valid_input_chars as UTF-8
- Use the encoding option from the .conf file always, not only in m17n mode
- Whether m17n mode is used should depend on the .conf file, not the language
- Use correct encoding to decode the dictionary file
- Some other minor fixes

* Wed Sep 26 2012 Anish Patil <apatil@redhat.com> - 0.0.10-1
- Upstream has released new version.

* Thu Sep 13 2012 Anish Patil <apatil@redhat.com> - 0.0.9-1
- Upstream has released new version.

* Tue Aug 14 2012 Anish Patil <apatil@redhat.com> - 0.0.8-1
- Upstream has released new version.

* Tue Jul 17 2012 Anish Patil <apatil@redhat.com> - 0.0.7-1
- The first version.
- derieved from ibus-table developed by Yu Yuwei <acevery@gmail.com>
