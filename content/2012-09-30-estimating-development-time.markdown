Title: Estimating Development Time?
Date: 2012-09-30T19:55:00+00:00
Slug: estimating-development-time
Category: 
Tags: 
Authors: Garry Bodsworth

<div class='post'>
It has been a crazy week where at the beginning nothing existed and on Friday the project was demoed live with all the functionality working. &nbsp;In this compressed five day lifecycle it brought into sharp clarity &nbsp;many aspects of software development. &nbsp;I've always been able to estimate project length but there was no science in it, I always operated on gut feeling and put in healthy margins of error.

I was one of the cogs in this project but before I go into breaking down the project there were some other factors helping this development be a success:

<ul><li>Someone leading the project who made sure requirements were locked down and made sure there was no feature creep (within reason).</li><li>Testers were on from day one, planning how to test and then seeing through all manner of test regimens.</li><li>Working with smart people.</li><li>Good tools for source code management, documentation, and bug tracking.</li></ul><div>The thing that was really scary for me as a project was how my time broke down:</div><div><ul><li>1 day coding</li><li>2 days integration</li><li>2 days testing and polishing</li></ul><div>The critical aspect here is I spent one day out of five working on pure code and design. &nbsp;This should be apparent to developers that coding is not the only task in delivering software projects. &nbsp;By getting something that was working in half a day also gave other people something real to code against rather than trying to hope integration would happen.</div></div><div>
</div><div>The next bit was two days of integration, this involved tidying up the code for deployment, working out installers, dependencies and so on. &nbsp;Then also it was a case of working out how all of this will work seamlessly for the end user. &nbsp;This also involved working out how certain bits of the operating system would work when you don't have user contexts to depend on that run as administrator, because after all most devs have their machines configured like this. &nbsp;Having this installer is critical for running proper end to end tests and ensuring the end-user will get the best experience.</div><div>
</div><div>Then we've got testing, this is unit-testing (well actually not a lot of that in a way), functional testing, and integration testing. On a tight deadline some of this is manual and not fully automated.</div><div>
</div><div>In amongst all this it was a case of making sure documentation was available for all aspects of the project, from end-user, through development and API right through to testing documents and lists of tests.</div><div>
</div><div>I suppose this thing that people reading this is if you work out how long it will take you to code, multiply that by five.</div></div>
