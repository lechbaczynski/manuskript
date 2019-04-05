# Change Log

## [0.9.0](https://github.com/olivierkes/manuskript/tree/0.9.0) (2019-04-04)

[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.8.0...0.9.0)

**Implemented enhancements:**

- Fullscreen editor suggestions [\#527](https://github.com/olivierkes/manuskript/issues/527)
- \[Feature Request\] Keyboard shortcuts in Full-Screen mode [\#444](https://github.com/olivierkes/manuskript/issues/444)
- \[Feature Request\] Add Ability to Add Image When Creating Fullscreen Theme [\#399](https://github.com/olivierkes/manuskript/issues/399)
- Making Fullscreen Mode Great Again [\#234](https://github.com/olivierkes/manuskript/issues/234)

**Fixed bugs:**

- Crash when previewing malformed regular expression when compiling [\#488](https://github.com/olivierkes/manuskript/issues/488)
- Spellcheck On/Off setting ignored / Manuskript unresponsive [\#474](https://github.com/olivierkes/manuskript/issues/474)
- Wrong codepage for import causes crash [\#470](https://github.com/olivierkes/manuskript/issues/470)
- Full-screen mode right-click menu black text on black background [\#440](https://github.com/olivierkes/manuskript/issues/440)
- Application language still the same after changing it in the settings. [\#411](https://github.com/olivierkes/manuskript/issues/411)

**Closed issues:**

- Python issues? lxml [\#541](https://github.com/olivierkes/manuskript/issues/541)
- Cannot open a project. [\#529](https://github.com/olivierkes/manuskript/issues/529)
- Corrupted Project File Crashes When Opening.  [\#522](https://github.com/olivierkes/manuskript/issues/522)
- Specific document suddenly won't open [\#502](https://github.com/olivierkes/manuskript/issues/502)
- trying to get pandoc to work manuskript 0.8.0 Win10 64 [\#475](https://github.com/olivierkes/manuskript/issues/475)
- Editor does not show text [\#472](https://github.com/olivierkes/manuskript/issues/472)
- Application crashes when trying to save "…" [\#461](https://github.com/olivierkes/manuskript/issues/461)
- Feature Request: script writing interface for manuskript  [\#435](https://github.com/olivierkes/manuskript/issues/435)
- Chinese translation filename suffix [\#428](https://github.com/olivierkes/manuskript/issues/428)

**Merged pull requests:**

- Fix color scheme of fullscreen editor [\#539](https://github.com/olivierkes/manuskript/pull/539) ([kakaroto](https://github.com/kakaroto))
- Directory entries in ZIP break loading code [\#531](https://github.com/olivierkes/manuskript/pull/531) ([worstje](https://github.com/worstje))
- Providing a suitable icon for consumption by Windows operating systems [\#530](https://github.com/olivierkes/manuskript/pull/530) ([worstje](https://github.com/worstje))
- Ensure text file open methods use utf-8 encoding [\#515](https://github.com/olivierkes/manuskript/pull/515) ([gedakc](https://github.com/gedakc))
- Fix crash when right-clicking twice on fullscreen panel in Windows 10 [\#514](https://github.com/olivierkes/manuskript/pull/514) ([kakaroto](https://github.com/kakaroto))
- Add support for IPython Jupyter QT Console as a debugging aid [\#513](https://github.com/olivierkes/manuskript/pull/513) ([kakaroto](https://github.com/kakaroto))
- Fix background of popup menus that were transparent \(black\) [\#512](https://github.com/olivierkes/manuskript/pull/512) ([kakaroto](https://github.com/kakaroto))
- Add snap build and package [\#511](https://github.com/olivierkes/manuskript/pull/511) ([tomwardill](https://github.com/tomwardill))
- Add ability to add new background images through UI. [\#510](https://github.com/olivierkes/manuskript/pull/510) ([kakaroto](https://github.com/kakaroto))
- Fullscreen panels improvements [\#509](https://github.com/olivierkes/manuskript/pull/509) ([kakaroto](https://github.com/kakaroto))
- Fix corkView background image on Windows [\#508](https://github.com/olivierkes/manuskript/pull/508) ([kakaroto](https://github.com/kakaroto))
- Do not default spellcheck to True for new editor views [\#506](https://github.com/olivierkes/manuskript/pull/506) ([kakaroto](https://github.com/kakaroto))
- Set editor theme stylesheet to QTextEdit only. [\#504](https://github.com/olivierkes/manuskript/pull/504) ([kakaroto](https://github.com/kakaroto))
- Fix fullscreen editor's myScrollBar delayed destruction causing a crash [\#503](https://github.com/olivierkes/manuskript/pull/503) ([kakaroto](https://github.com/kakaroto))
- 2nd try to fix macOS X blank screen when leaving fullscreen editor mode [\#495](https://github.com/olivierkes/manuskript/pull/495) ([gedakc](https://github.com/gedakc))
- Fix crash when right clicking a word in editor and enchant is not installed [\#492](https://github.com/olivierkes/manuskript/pull/492) ([kakaroto](https://github.com/kakaroto))
- Don't crash if a typo is made in the exporter's regular expression. [\#486](https://github.com/olivierkes/manuskript/pull/486) ([kakaroto](https://github.com/kakaroto))
- Fix crash when previewing pandoc HTML with QTextEdit as web renderer… [\#485](https://github.com/olivierkes/manuskript/pull/485) ([kakaroto](https://github.com/kakaroto))
- Fix crash when 7 pound signs are written alone on a line. [\#484](https://github.com/olivierkes/manuskript/pull/484) ([kakaroto](https://github.com/kakaroto))
- Try to fix macOS X blank screen when leaving editor fullscreen mode [\#482](https://github.com/olivierkes/manuskript/pull/482) ([gedakc](https://github.com/gedakc))
- Fix wrong codepage crash on import with Windows 10 [\#478](https://github.com/olivierkes/manuskript/pull/478) ([gedakc](https://github.com/gedakc))
- Spelling: Manuscript, may have to be restarted [\#454](https://github.com/olivierkes/manuskript/pull/454) ([comradekingu](https://github.com/comradekingu))
- Chinese translation [\#434](https://github.com/olivierkes/manuskript/pull/434) ([lingsamuel](https://github.com/lingsamuel))
- fix translator [\#433](https://github.com/olivierkes/manuskript/pull/433) ([lingsamuel](https://github.com/lingsamuel))
- Remember last accessed directory [\#431](https://github.com/olivierkes/manuskript/pull/431) ([lingsamuel](https://github.com/lingsamuel))
- translation suffix, change translation load order [\#430](https://github.com/olivierkes/manuskript/pull/430) ([lingsamuel](https://github.com/lingsamuel))

## [0.8.0](https://github.com/olivierkes/manuskript/tree/0.8.0) (2018-12-05)
[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.7.0...0.8.0)

**Fixed bugs:**

- Snowflake Method option is greyed out. [\#419](https://github.com/olivierkes/manuskript/issues/419)
- Plots bounce around main, secondary, and minor -- unsatisfactory solution? [\#404](https://github.com/olivierkes/manuskript/issues/404)
- Segmentation fault on import [\#402](https://github.com/olivierkes/manuskript/issues/402)
- "Corrupted" settings and impossibility to start [\#377](https://github.com/olivierkes/manuskript/issues/377)
- Resolution step deleting itself on pressing Ctrl + Backspace [\#375](https://github.com/olivierkes/manuskript/issues/375)
- Develop Branch Crashes in Outline View [\#355](https://github.com/olivierkes/manuskript/issues/355)
- Export crashes, because of encoding to 1250 [\#331](https://github.com/olivierkes/manuskript/issues/331)
- pandoc v2 has deprecated some options and extensions so manuskript is giving error. [\#304](https://github.com/olivierkes/manuskript/issues/304)
- Compile Issue for Pandoc Formats - pandoc.exe incorrect [\#186](https://github.com/olivierkes/manuskript/issues/186)

**Closed issues:**

- Problems with running from 0.7.0 pyinstaller package on mac os x 10.13 [\#386](https://github.com/olivierkes/manuskript/issues/386)
- Old bugs in current version 0.6.0 \(with crosslinks and details\) [\#371](https://github.com/olivierkes/manuskript/issues/371)
- pt\_PT translation and Weblate [\#408](https://github.com/olivierkes/manuskript/issues/408)
- Italian translation [\#395](https://github.com/olivierkes/manuskript/issues/395)
- Snowflake view mode always disabled [\#45](https://github.com/olivierkes/manuskript/issues/45)

**Merged pull requests:**

- Remove unimplemented snowflake view mode menu entry [\#424](https://github.com/olivierkes/manuskript/pull/424) ([gedakc](https://github.com/gedakc))
- Increase Travis CI macOS X build minimum to Sierra \(10.12\) [\#423](https://github.com/olivierkes/manuskript/pull/423) ([gedakc](https://github.com/gedakc))
- Remove plot resolution step key bindings Ctrl+Enter and Ctrl+Backspace [\#420](https://github.com/olivierkes/manuskript/pull/420) ([gedakc](https://github.com/gedakc))
- Add support for pandoc version 2 [\#418](https://github.com/olivierkes/manuskript/pull/418) ([gedakc](https://github.com/gedakc))
- Prevent build and deploy steps for linux on Travis CI [\#414](https://github.com/olivierkes/manuskript/pull/414) ([gedakc](https://github.com/gedakc))
- Limit pyinstaller package build and deploy to osx on Travis CI [\#413](https://github.com/olivierkes/manuskript/pull/413) ([gedakc](https://github.com/gedakc))
- Fix segmentation fault on import [\#412](https://github.com/olivierkes/manuskript/pull/412) ([gedakc](https://github.com/gedakc))
- Fix pytest warnings [\#407](https://github.com/olivierkes/manuskript/pull/407) ([gedakc](https://github.com/gedakc))
- Fix plot importance changes if delete earlier plot and click other plots [\#406](https://github.com/olivierkes/manuskript/pull/406) ([gedakc](https://github.com/gedakc))
- Enable testing in TravisCI [\#403](https://github.com/olivierkes/manuskript/pull/403) ([katafrakt](https://github.com/katafrakt))
- Fix Travis CI build for Mac OSX - pip3: command not found [\#400](https://github.com/olivierkes/manuskript/pull/400) ([gedakc](https://github.com/gedakc))
- Moved incorrectly placed parameter to correct place. Closes \#377. [\#389](https://github.com/olivierkes/manuskript/pull/389) ([RiderExMachina](https://github.com/RiderExMachina))

## [0.7.0](https://github.com/olivierkes/manuskript/tree/0.7.0) (2018-08-15)
[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.6.0...0.7.0)

**Implemented enhancements:**

- Display images as tooltip [\#270](https://github.com/olivierkes/manuskript/issues/270)
- Focus mode [\#259](https://github.com/olivierkes/manuskript/issues/259)
- Add markdown support of other tabs [\#232](https://github.com/olivierkes/manuskript/issues/232)
- Translation automation [\#228](https://github.com/olivierkes/manuskript/issues/228)
- Add: command line parameter to open project [\#223](https://github.com/olivierkes/manuskript/issues/223)
- Moving World Items [\#219](https://github.com/olivierkes/manuskript/issues/219)
- Make http links clickable in markdown editor [\#215](https://github.com/olivierkes/manuskript/issues/215)
- Feature suggestion: Typewriter scrolling. [\#175](https://github.com/olivierkes/manuskript/issues/175)
- Request for Bullets and Numbering option [\#123](https://github.com/olivierkes/manuskript/issues/123)
- Markdown syntax highlighting [\#13](https://github.com/olivierkes/manuskript/issues/13)
- Add moving World Items [\#298](https://github.com/olivierkes/manuskript/pull/298) ([JackXVII](https://github.com/JackXVII))

**Fixed bugs:**

- Install on MacOsX failed [\#282](https://github.com/olivierkes/manuskript/issues/282)
- Crash if Cheatsheet filter term not found and Enter key pressed [\#354](https://github.com/olivierkes/manuskript/issues/354)
- Overlay status bar prevents access to add/delete world item icons when displaying a message [\#307](https://github.com/olivierkes/manuskript/issues/307)
- Deleting multiple World items leaves/creates two empty items [\#306](https://github.com/olivierkes/manuskript/issues/306)
- Underline causes false spelling error [\#283](https://github.com/olivierkes/manuskript/issues/283)
- .DS\_Store files let crash Manuskript when opening project [\#281](https://github.com/olivierkes/manuskript/issues/281)
- Programm killed by Hovereffekt? [\#275](https://github.com/olivierkes/manuskript/issues/275)
- Spell check is crashing the program [\#273](https://github.com/olivierkes/manuskript/issues/273)
- Highlight Contrast Problem [\#272](https://github.com/olivierkes/manuskript/issues/272)
- Segfault when pasting text with focus mode enabled [\#271](https://github.com/olivierkes/manuskript/issues/271)
- Compile Check Box not working in Outline view [\#263](https://github.com/olivierkes/manuskript/issues/263)
- Manuskript response slow with recent addition of focus mode [\#261](https://github.com/olivierkes/manuskript/issues/261)
- Organize Menu is not disabled on startup [\#260](https://github.com/olivierkes/manuskript/issues/260)
- Ctrl+tab gets trapped in Debug tab [\#249](https://github.com/olivierkes/manuskript/issues/249)
- Index card status can spillover [\#246](https://github.com/olivierkes/manuskript/issues/246)
- Cannot write a summary on a plot resolution step [\#240](https://github.com/olivierkes/manuskript/issues/240)
- Format buttons in text editor window not working [\#59](https://github.com/olivierkes/manuskript/issues/59)
- stop crash when click btnGoUp and current editor is None [\#318](https://github.com/olivierkes/manuskript/pull/318) ([Windspar](https://github.com/Windspar))
- Avoid crash on spellcheck by ensuring enchant dictionary exists [\#303](https://github.com/olivierkes/manuskript/pull/303) ([gedakc](https://github.com/gedakc))
- Skip loading directory and file names that begin with a period [\#302](https://github.com/olivierkes/manuskript/pull/302) ([gedakc](https://github.com/gedakc))

**Closed issues:**

- \[Feature request\] Russian translation [\#358](https://github.com/olivierkes/manuskript/issues/358)
- Manuskript crashes during save process and "corrupts" the msk-file [\#352](https://github.com/olivierkes/manuskript/issues/352)
- Add polish translation  [\#289](https://github.com/olivierkes/manuskript/issues/289)
- \[Feature request\] Accept first command line argument as project file name to open [\#278](https://github.com/olivierkes/manuskript/issues/278)
- Status bar distracting when saving with current develop branch [\#262](https://github.com/olivierkes/manuskript/issues/262)
- Editor Consistency [\#257](https://github.com/olivierkes/manuskript/issues/257)
- French Tab in English Mode [\#253](https://github.com/olivierkes/manuskript/issues/253)
- I want to translate it to portuguese [\#230](https://github.com/olivierkes/manuskript/issues/230)

**Merged pull requests:**

- Fix Travix CI build error on OSX installing python3 [\#338](https://github.com/olivierkes/manuskript/pull/338) ([gedakc](https://github.com/gedakc))
- Use QPersistentModelIndex in textEditView [\#308](https://github.com/olivierkes/manuskript/pull/308) ([JackXVII](https://github.com/JackXVII))
- Add automated script to create RPM package [\#368](https://github.com/olivierkes/manuskript/pull/368) ([gedakc](https://github.com/gedakc))
- Build MacOS release with XCode 7.3 image [\#287](https://github.com/olivierkes/manuskript/pull/287) ([katafrakt](https://github.com/katafrakt))

## [0.6.0](https://github.com/olivierkes/manuskript/tree/0.6.0) (2017-11-29)
[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.5.0...0.6.0)

**Implemented enhancements:**

- Adds: document menu \(copy, paste, delete, duplicate, split, merge, etc.\) [\#229](https://github.com/olivierkes/manuskript/issues/229)
- Add transparent text editor [\#216](https://github.com/olivierkes/manuskript/issues/216)
- Add Mind Map Import [\#208](https://github.com/olivierkes/manuskript/issues/208)
- Adds: Importer \(docx, html, opml, …\) [\#200](https://github.com/olivierkes/manuskript/issues/200)
- Add a "Rename Item" option to context menu in the Tree view [\#189](https://github.com/olivierkes/manuskript/issues/189)
- Pandoc output: add more custom settings [\#173](https://github.com/olivierkes/manuskript/issues/173)

**Fixed bugs:**

- Manuskript fails to run in Ubuntu 14.04 [\#225](https://github.com/olivierkes/manuskript/issues/225)
- Program Crash on Import with images [\#213](https://github.com/olivierkes/manuskript/issues/213)
- Missing default file extension when Saving As... [\#211](https://github.com/olivierkes/manuskript/issues/211)
- One white pixel visible in full screen mode [\#210](https://github.com/olivierkes/manuskript/issues/210)
- Accentueted characters on linux [\#207](https://github.com/olivierkes/manuskript/issues/207)
- Manuskript crashes when creating new document on Ubuntu [\#198](https://github.com/olivierkes/manuskript/issues/198)
- Editor tab should trim long titles [\#194](https://github.com/olivierkes/manuskript/issues/194)
- Manuskript does not start with PyEnchant on MacOS [\#188](https://github.com/olivierkes/manuskript/issues/188)
- Index card text almost invisible in dark themes. [\#183](https://github.com/olivierkes/manuskript/issues/183)
- Accented characters not working [\#141](https://github.com/olivierkes/manuskript/issues/141)
- Accent not working [\#105](https://github.com/olivierkes/manuskript/issues/105)
- Accent marks not working [\#58](https://github.com/olivierkes/manuskript/issues/58)

**Closed issues:**

- new dalolog icon [\#237](https://github.com/olivierkes/manuskript/issues/237)
- Cannot select folder on create new project [\#224](https://github.com/olivierkes/manuskript/issues/224)
- Should pandoc be bundled with manuskript's packages? [\#190](https://github.com/olivierkes/manuskript/issues/190)
- Odd word choices in English - Take 2 [\#181](https://github.com/olivierkes/manuskript/issues/181)

**Merged pull requests:**

- Change words issue 181 [\#231](https://github.com/olivierkes/manuskript/pull/231) ([gedakc](https://github.com/gedakc))
- Add PyEnchant support to OSX builds [\#212](https://github.com/olivierkes/manuskript/pull/212) ([katafrakt](https://github.com/katafrakt))
- Update README.md for 0.5.0 release [\#205](https://github.com/olivierkes/manuskript/pull/205) ([gedakc](https://github.com/gedakc))
- \[WIP\] Add Travis CI support [\#203](https://github.com/olivierkes/manuskript/pull/203) ([katafrakt](https://github.com/katafrakt))
- Get default enchant Dict language in more reliable way [\#202](https://github.com/olivierkes/manuskript/pull/202) ([katafrakt](https://github.com/katafrakt))
- Expand german translation [\#193](https://github.com/olivierkes/manuskript/pull/193) ([ScullyBlue](https://github.com/ScullyBlue))
- Adds: Import OPML [\#192](https://github.com/olivierkes/manuskript/pull/192) ([camstevenson](https://github.com/camstevenson))

## [0.5.0](https://github.com/olivierkes/manuskript/tree/0.5.0) (2017-10-31)
[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.4.0...0.5.0)

**Implemented enhancements:**

- Swedish translation \(sv-SE\). [\#177](https://github.com/olivierkes/manuskript/issues/177)
- Spanish transalation for manuskript 0.5.0 [\#174](https://github.com/olivierkes/manuskript/issues/174)
- Suggestion: Configurable editor margins. [\#168](https://github.com/olivierkes/manuskript/issues/168)
- Feature request: disable cursor blinking [\#165](https://github.com/olivierkes/manuskript/issues/165)
- Suggestion: Block insertion cursor. [\#163](https://github.com/olivierkes/manuskript/issues/163)
- New navigation icon design [\#159](https://github.com/olivierkes/manuskript/issues/159)
- New flash card design [\#158](https://github.com/olivierkes/manuskript/issues/158)
- Redaction view navigation improvements [\#157](https://github.com/olivierkes/manuskript/issues/157)
- Request: Justified formatting of text [\#148](https://github.com/olivierkes/manuskript/issues/148)
- Ability to always show word target in distraction free mode [\#109](https://github.com/olivierkes/manuskript/issues/109)
- Use on smaller resolution screens [\#108](https://github.com/olivierkes/manuskript/issues/108)
- Odd wordchoices in English. [\#53](https://github.com/olivierkes/manuskript/issues/53)

**Fixed bugs:**

- Bug in 'World' section [\#126](https://github.com/olivierkes/manuskript/issues/126)
- Redaction's tab problem in 0.3.0 win version [\#92](https://github.com/olivierkes/manuskript/issues/92)
- Application Style setting GTK+ on Linux Mint Mate  [\#57](https://github.com/olivierkes/manuskript/issues/57)
- Likes to freeze and crash [\#50](https://github.com/olivierkes/manuskript/issues/50)
- Seg faults found [\#9](https://github.com/olivierkes/manuskript/issues/9)
- Installation - Qt platforn plugin "xcb" not found [\#8](https://github.com/olivierkes/manuskript/issues/8)
- Untranslatable strings. [\#178](https://github.com/olivierkes/manuskript/issues/178)
- Create new project ignores changes made to template levels before Create [\#171](https://github.com/olivierkes/manuskript/issues/171)
- Several bugs in drag'n'dropping items [\#169](https://github.com/olivierkes/manuskript/issues/169)
- Some panels require initial two clicks of RHS tab to hide [\#167](https://github.com/olivierkes/manuskript/issues/167)
- Spell checker is active for partial words. [\#166](https://github.com/olivierkes/manuskript/issues/166)
- Spell checking works but does not underline misspelled words [\#147](https://github.com/olivierkes/manuskript/issues/147)
- Contrast Problem in Notes/Refences with Dark Background [\#143](https://github.com/olivierkes/manuskript/issues/143)
- Crash when permissions don't allow saving [\#138](https://github.com/olivierkes/manuskript/issues/138)
- App crash when moving a step in Plots section [\#134](https://github.com/olivierkes/manuskript/issues/134)
- Indent not saved in custom full screen theme [\#133](https://github.com/olivierkes/manuskript/issues/133)
- 'Save as' only partly works [\#128](https://github.com/olivierkes/manuskript/issues/128)
- "pandoc: Could not parse YAML header" error [\#124](https://github.com/olivierkes/manuskript/issues/124)
- Distraction free mode crashes with time target [\#119](https://github.com/olivierkes/manuskript/issues/119)
- Pandoc PDF output error with unicode characters [\#117](https://github.com/olivierkes/manuskript/issues/117)
- Character Importance-Slider memorize importance of last character ... partly [\#102](https://github.com/olivierkes/manuskript/issues/102)
- Index cards seem to keep a background image by default. [\#52](https://github.com/olivierkes/manuskript/issues/52)
- In revision mode text, selecting group doesn't load text-preferences right. [\#51](https://github.com/olivierkes/manuskript/issues/51)
- Undo/redo works in some text areas but not others [\#34](https://github.com/olivierkes/manuskript/issues/34)
- Some bugs in Windows XP and Ubuntu 15.1 [\#25](https://github.com/olivierkes/manuskript/issues/25)
- Stylesheet error on windows [\#18](https://github.com/olivierkes/manuskript/issues/18)
- Manuskript fails to load last state of panels [\#14](https://github.com/olivierkes/manuskript/issues/14)
- Multiple selections of items sometimes gets Notes/references field to be ereased [\#10](https://github.com/olivierkes/manuskript/issues/10)

**Closed issues:**

- Cannot start manuskript due to import error [\#179](https://github.com/olivierkes/manuskript/issues/179)
- Does not run on Ubuntu 17.10 [\#170](https://github.com/olivierkes/manuskript/issues/170)
- Add translation with transifex.com [\#140](https://github.com/olivierkes/manuskript/issues/140)
- Site of Manuskript is not in the air at the moment [\#139](https://github.com/olivierkes/manuskript/issues/139)
- Manuskript Fail to Launch After Several Successes on Windows 10 [\#132](https://github.com/olivierkes/manuskript/issues/132)
- Index Card Background Freeze [\#127](https://github.com/olivierkes/manuskript/issues/127)
- Keyboard shortcuts aren't functioning, No undo feature.   [\#125](https://github.com/olivierkes/manuskript/issues/125)
- Trojan in current windows installer? [\#112](https://github.com/olivierkes/manuskript/issues/112)
- Manuskript no longer opening [\#106](https://github.com/olivierkes/manuskript/issues/106)
- not working on Mac [\#35](https://github.com/olivierkes/manuskript/issues/35)

**Merged pull requests:**

- Change message from warning to note for failed to load translator string [\#110](https://github.com/olivierkes/manuskript/pull/110) ([gedakc](https://github.com/gedakc))
- Add about manuskript dialog [\#153](https://github.com/olivierkes/manuskript/pull/153) ([gedakc](https://github.com/gedakc))
- Add help tip for world tab [\#151](https://github.com/olivierkes/manuskript/pull/151) ([gedakc](https://github.com/gedakc))
- Add missing \_\_init\_\_.py file [\#149](https://github.com/olivierkes/manuskript/pull/149) ([gedakc](https://github.com/gedakc))
- Fixes: Manuskript fails to load last state of panels [\#136](https://github.com/olivierkes/manuskript/pull/136) ([gedakc](https://github.com/gedakc))
- Add to README a HowTo section with link to Wiki [\#131](https://github.com/olivierkes/manuskript/pull/131) ([gedakc](https://github.com/gedakc))
- Fixes: Contents missing when non-single file project saved with Save as [\#129](https://github.com/olivierkes/manuskript/pull/129) ([gedakc](https://github.com/gedakc))
- Fixes: add character button does not set importance slider to default… [\#121](https://github.com/olivierkes/manuskript/pull/121) ([gedakc](https://github.com/gedakc))
- Request confirmation if create project would overwrite existing file\(s\) [\#114](https://github.com/olivierkes/manuskript/pull/114) ([gedakc](https://github.com/gedakc))
- Fixes: Unable to change index cards background from image to a color [\#113](https://github.com/olivierkes/manuskript/pull/113) ([gedakc](https://github.com/gedakc))
- Add project name to main window title [\#103](https://github.com/olivierkes/manuskript/pull/103) ([gedakc](https://github.com/gedakc))
- Fixes: after project close, open or create project fails [\#100](https://github.com/olivierkes/manuskript/pull/100) ([gedakc](https://github.com/gedakc))
- Fixes: incorrect reference to 32px icon [\#97](https://github.com/olivierkes/manuskript/pull/97) ([gedakc](https://github.com/gedakc))

## [0.4.0](https://github.com/olivierkes/manuskript/tree/0.4.0) (2017-05-25)
[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.3.0...0.4.0)

**Implemented enhancements:**

- Export into text? \[feature suggestion\] [\#80](https://github.com/olivierkes/manuskript/issues/80)
- Default background for fullscreen mode is unusable \[minor\] [\#79](https://github.com/olivierkes/manuskript/issues/79)
- Documention Needed [\#69](https://github.com/olivierkes/manuskript/issues/69)
- Compile dialog issues: cancel doesn't seem to do anything, default ouput directory wrong [\#77](https://github.com/olivierkes/manuskript/issues/77)
- OS X app with Platypus [\#28](https://github.com/olivierkes/manuskript/issues/28)

**Fixed bugs:**

- Unable to type the "ê" character [\#46](https://github.com/olivierkes/manuskript/issues/46)
- Bug: File doesn't open if spellcheck is active and dictionary is missing [\#26](https://github.com/olivierkes/manuskript/issues/26)
- Installed PyEnchant but Manuskript still asks me to "Install PyEnchant to use Spellcheck" [\#122](https://github.com/olivierkes/manuskript/issues/122)
- Crashes when trying to create or open the project [\#99](https://github.com/olivierkes/manuskript/issues/99)
- After close project, open or create project fails [\#96](https://github.com/olivierkes/manuskript/issues/96)
- Crash on create - Linux Mint 18 [\#91](https://github.com/olivierkes/manuskript/issues/91)
- Compile not honoring check marks [\#90](https://github.com/olivierkes/manuskript/issues/90)
- Plots, resolutions steps screen: columns not sizeable. [\#87](https://github.com/olivierkes/manuskript/issues/87)
- word count [\#72](https://github.com/olivierkes/manuskript/issues/72)
- Cant create a new project using Ubuntu 16.10 [\#70](https://github.com/olivierkes/manuskript/issues/70)
- Fails to create a project in Linux [\#65](https://github.com/olivierkes/manuskript/issues/65)
- does not compile to OpenOffice format [\#61](https://github.com/olivierkes/manuskript/issues/61)
- Doesn't save in redaction [\#55](https://github.com/olivierkes/manuskript/issues/55)
- Error "Fail to load translator..." [\#49](https://github.com/olivierkes/manuskript/issues/49)
- Crash at project creation on mac [\#48](https://github.com/olivierkes/manuskript/issues/48)
- crash on create new project [\#44](https://github.com/olivierkes/manuskript/issues/44)
- epiphany section in basic infos for characters not saved [\#43](https://github.com/olivierkes/manuskript/issues/43)
- 0.3.0 File Creation Issues [\#37](https://github.com/olivierkes/manuskript/issues/37)
- Can't create new project on Linux [\#30](https://github.com/olivierkes/manuskript/issues/30)
- Problem with minimum size of program window? [\#29](https://github.com/olivierkes/manuskript/issues/29)
- Bug: Writing a .msk file in linux and opening it in windows clean the outline files [\#27](https://github.com/olivierkes/manuskript/issues/27)
- Welcome windows on OS X: single click instead of double click [\#23](https://github.com/olivierkes/manuskript/issues/23)
- AttributeError in editorWidget [\#11](https://github.com/olivierkes/manuskript/issues/11)

**Closed issues:**

- File creation fails and causes Manuskript to crash [\#93](https://github.com/olivierkes/manuskript/issues/93)
- Failed to load translator [\#89](https://github.com/olivierkes/manuskript/issues/89)
- crashing on initial save \(again?\) [\#88](https://github.com/olivierkes/manuskript/issues/88)
- Impossible to start a project on Lubuntu 16.04 [\#85](https://github.com/olivierkes/manuskript/issues/85)
- Manuskript 0.3.0 crash on Windows 10 [\#83](https://github.com/olivierkes/manuskript/issues/83)
- on Fedora 25 Manuskript doesn't start [\#82](https://github.com/olivierkes/manuskript/issues/82)
- \(l\)ubuntu dependencies for develop branch [\#81](https://github.com/olivierkes/manuskript/issues/81)
- Creating new project fails [\#76](https://github.com/olivierkes/manuskript/issues/76)
- Missing module when launching from github \[Xubuntu 16.04.1 LTS\] [\#73](https://github.com/olivierkes/manuskript/issues/73)
- Download does not run on 32bit Linux [\#63](https://github.com/olivierkes/manuskript/issues/63)
- Locale Warning [\#62](https://github.com/olivierkes/manuskript/issues/62)
- Crashes when creating new project [\#60](https://github.com/olivierkes/manuskript/issues/60)
- Is This An Active Project [\#56](https://github.com/olivierkes/manuskript/issues/56)
- Qt WebKit is deprecated [\#54](https://github.com/olivierkes/manuskript/issues/54)
- Unable to run application [\#47](https://github.com/olivierkes/manuskript/issues/47)
- \[Windows\] Compile Dialog does not have a title [\#39](https://github.com/olivierkes/manuskript/issues/39)
- Creating manuskript binay for Android and IOS [\#21](https://github.com/olivierkes/manuskript/issues/21)
- Compiling Manuskript in windows [\#19](https://github.com/olivierkes/manuskript/issues/19)
- No distance between two scenes in compiled document [\#104](https://github.com/olivierkes/manuskript/issues/104)
- Small typographic error in the README [\#84](https://github.com/olivierkes/manuskript/issues/84)
- \[Windows\] HTML compiled file title is "FIXME" [\#42](https://github.com/olivierkes/manuskript/issues/42)
- \[Windows\] Compile operation does not adds the file extension when the file type option is changed [\#41](https://github.com/olivierkes/manuskript/issues/41)
- \[Windows\] Compile dialog comes with development machine default location [\#40](https://github.com/olivierkes/manuskript/issues/40)
- \[Windows\] Cancel Button on Compile Dialog does not work [\#38](https://github.com/olivierkes/manuskript/issues/38)

**Merged pull requests:**

- Fixes: field "Source of conflict" in World is not active [\#95](https://github.com/olivierkes/manuskript/pull/95) ([gedakc](https://github.com/gedakc))
- Fixes: epiphany section in basic infos for characters not saved \#43 [\#94](https://github.com/olivierkes/manuskript/pull/94) ([gedakc](https://github.com/gedakc))
- Updating README.md [\#68](https://github.com/olivierkes/manuskript/pull/68) ([olivierkes](https://github.com/olivierkes))
- added commands to install dependencies to README [\#67](https://github.com/olivierkes/manuskript/pull/67) ([wmww](https://github.com/wmww))
- Added spanish translation \(and changed "chuleta" for "guía rápida"\). [\#66](https://github.com/olivierkes/manuskript/pull/66) ([jmgaguilera](https://github.com/jmgaguilera))

## [0.3.0](https://github.com/olivierkes/manuskript/tree/0.3.0) (2016-03-31)
[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.2.0...0.3.0)

**Fixed bugs:**

- Windows package fails antivirus scan [\#15](https://github.com/olivierkes/manuskript/issues/15)
- DictNotFoundError when dict language specified in settings is not installed [\#12](https://github.com/olivierkes/manuskript/issues/12)
- Manuskript fails to lauch on Windows [\#7](https://github.com/olivierkes/manuskript/issues/7)
- The plot line colours keep changing? [\#6](https://github.com/olivierkes/manuskript/issues/6)

**Closed issues:**

- Windows installation issue [\#16](https://github.com/olivierkes/manuskript/issues/16)

## [0.2.0](https://github.com/olivierkes/manuskript/tree/0.2.0) (2016-02-28)
[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.1.1...0.2.0)

**Fixed bugs:**

- Fullscreen editor error when text is empty \(wordcount = 0\) [\#3](https://github.com/olivierkes/manuskript/issues/3)
- Save file doesn't automatically add .msk [\#2](https://github.com/olivierkes/manuskript/issues/2)

## [0.1.1](https://github.com/olivierkes/manuskript/tree/0.1.1) (2016-02-08)
[Full Changelog](https://github.com/olivierkes/manuskript/compare/0.1.0...0.1.1)

**Fixed bugs:**

- Crash on initial save [\#1](https://github.com/olivierkes/manuskript/issues/1)

## [0.1.0](https://github.com/olivierkes/manuskript/tree/0.1.0) (2016-02-06)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*
