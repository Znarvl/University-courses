# Lab 3: Software construction - Cross-platform, localization and internationalization
---
by: Simon Jakobsson (simja649) and Axel Gard (axega544)

## 1. unicode
**Answer what happened before you modified the code and why?** \
Answer: It executed the file on linux but the exe ended up in a loop on windows.
With wine got a `0021:err:environ:run_wineboot boot event wait timed out`.
The reason behind this is that linux can read UTF-8 and Windows can not.


## reflection from semi 4
We discussed the value of using cross-platform. We discussed when it is necessary
to use native language in an application and when it is better to use a framework
(like react native or Qt) to have cross platform viability and when is it not needed,
like when you only need to use a few libraries or when not using user interfaces.

We changed our lab code just a little bit. We discussed with the other group how to use
the args to select src file and dest file. So we changed how we set the destination file
to use argv[1]. Otherwise nothing was changed beside some better spacing and removed
some commented out old code.

Reading documentations was maybe our weakness in this lab because we had a hard time to
use the right tools to get the copy files and translation done. When we got on the right
track we understood quickly that it was not that hard to implement the tasks.
Probably the most difficult part of the labb was the translation exercises,
because the set of tools that was needed for the exercise nighter one of us had
any experience with whatsoever.

We did not actually feel unprepared for this lab even if we thought it was harder
than the previous ones. The hard part of this lab is probably due to the fact that
the windows documentation is basically your only option in comparison to the other labs.  

For the most part we agreed with each other when we presented the results and argued
about cross-platform usage and non-usage. In the case of mobile development then the
usage of a cross platform framework (react navitve, unity etc) is an alternative to
not having to code for multiple platforms but comes with the drawback of bloated
applications. So the question here is whether it is worth sacrificing memory for
cross-platform usage. Sometimes it might sometimes not.
