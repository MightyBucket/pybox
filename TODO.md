TODO ASAP
==
 - [x] Add errors list to record errors (tools > plexer.py)
 - [x] Add syntax coloring to editor (tools > Blitz.py) using the results from the plexer (tools > plexer.py)
 - [x] Stress test error list and bug fix syntax coloring (tools > Blitz.py)
 - [x] Tidy up the output from printed text (tools > *)
 - [x] Fix `TAB` token bug
 - [ ] Add `EOF` token recognition to the plexer (tools > plexer.py)
 - [ ] Stress test token creation and bug fix the post-processor (tools > PP.py)
 - [ ] Improve the Blitz engine (tools > Blitz.py) to allow for better rendering
 - [ ] Add more colors to the editor (tools > Blitz.py) and make it more modern
 - [ ] Create the extension engine (pex > pex_loader.py)
 - [ ] Stress test syntax coloring
 - [ ] Add functional buttons to the editor

TODO LONG-TERM
==
 - [ ] Enable the extension engine
 - [ ] Add extension-builder capability
 - [ ] Stress test

STRESS TEST RESULTS
==
| Function Tested | Expected | Outcome | Improvements |
-------------------------------------------------------
| Error detection and collection | Errors to be recorded when detected | Errors were recorded but list does not clear | Ensure list clears on new build |
| Token creation  | Tokens created as expected | Tokens were created as expected | No improvements necessary atm |