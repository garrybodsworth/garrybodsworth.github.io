Title: CV
Date: 2016-01-02 04:16

# Garry James Bodsworth

I’m a versatile engineer and technical lead always looking to improve development. Currently I build secure web browsers on a variety of platforms using multiple rendering engines (WebKit/Trident/Gecko). I’ve developed web services, desktop applications, and Linux distributions. Core areas of expertise include C/C++, Python, Django, networking, security, testing, deployment, web browsers and web technologies. I can pick up new technologies quickly as with Azure and C# at Microsoft and with Objective-C on OSX. I care about the whole development process beyond simply writing code through testing, deployment and delivering to customers.


## Skills

- **Programming Languages**: C, C++, C#, .NET, Objective-C, Python

- **Web Technologies**: Django, AWS, HTML, JavaScript, XML, Twitter Bootstrap, Databases (MySQL/PostGreSQL/MS-SQL), Webservers (nginx/Apache/Twisted), Fabric, VirtualEnv, Message queues (RabbitMQ/Celery), Templating engines (Jinja2)

- **Continuous Integration**: Jenkins, CMake

- **Process**: Agile, Bug trackers, Planning/Roadmaps

- **Platforms**: Windows, Linux, Mac OS X

- **Testing**: TDD, Unit testing, Selenium, Ïntegration testing, GTest, py.test



## Employment

### *Member of Technical Staff*, Bromium
<small>Jan 2014 — ongoing</small>
Bromium is a computer endpoint security company. During my second spell at Bromium I have mainly been working on ensuring technology and products are the quality required for customers to deploy.

- Currently working on the IE team to improve the quality of the product

- Running the team’s development sprints involving planning, execution and tracking.

- Ensuring the browser features were implemented or worked correctly for cookies, redirects, DOM storage, history and most areas of browser technology.

- Expertise in networking, specifically for browser, in proxies, HTTP, TCP, DNS, etc.

- Currently running, tracking and organising the team's sprint process.

- A founding member of the architecture group to help steer the technical direction of the company.

- Implemented protected mode, enhanced protected mode (EPM), full 64-bit browser mode.

- Securing IE using the extension and plugin technologies ActiveX, ActiveDocument, COM, BHO, APP and download managers.

- Reverse-engineering the platform browser and using WinDBG to solve difficult bugs.

- Removed 2.7 million lines of code whilst adding features.

- Helped to build the new Selenium-based test framework for the browser. Wrote the pure Python test server that is specifically designed to perform self-contained reproducible examples. This involves dynamic resigning of SSL/HTTPS whilst vhosting domains on a single IP. Supplied hundreds of tests across multiple browsers for functionality and regressions, many examples require studying how web pages were built and extracting the minimal reproduction code.

- Worked on the OS X team on a variety of features and projects using C++ and Objective-C

- Graphics performance and robustness in OpenGL working on a seamless graphics application technology.

- Helping to build the secure Safari web browser using plugins, extensions, Javascript, HTML, CSS, as well as editing WebKit.

- The remote configuration engine built on a cross-platform C++ library and an Objective-C interface.  Using XML (SAX), C++11, GTest, Gcovr, lcov, gyp, Cmake, Xcode, Xcode unit-testing, XSLT, XSD, and a bunch of other stuff.  Test code has been critical for making this work properly first time on a tight timescale.

- Created a new Developer Quickstart guide involving fixing build and dependencies to let developers get productive as soon as possible.

### *Senior Server Engineer - Security*, Microsoft - Lift London
<small>Jun 2013 — Dec 2013</small>
Lift London were a separate start-up inside of Microsoft making new gaming experiences on new platforms. This required a new webservices team where I contributed to all areas and my core remit was security.

- Working on the services team building a massively scalable web backend for computer games. This involves using Azure, .NET framework and C#. The code involved heavy use of asynchronous programming and Azure Tables.

- I built the new communication protocol for better security derived from the best parts of OAuth 1.0a and 2.0. This was covered with extensive testing and threat modelling.

- Built an integration test framework for faster more comprehensive testing. This allowed the feedback loop for developers to get much tighter in order to develop at a faster pace. It involved factoring out the server and Azure dependencies. These tests then were abe to provide concise documentation for the APIs by the test implementations.

- I designed and built social login and accounts, user models, the configuration service, and general libraries to avoid duplicating code. I was responsible for DNS, SSL/HTTPS, deployment and other network related areas.

- Other things I did was research into technologies like load-balancers on Azure, logging infrastructure. I also wrote a minimal JSON parsing library specifically to avoid all the problems of .NET JSON parsers (garbage collection, reflection causing performance issues) which I contributed to the code sharing project internally.

- I ran the code sharing initiative within Microsoft Studios to improve communication and code reuse due to my knowledge and use of open-source technologies. Lift London lead the way in this area within the Microsoft Studios.

### *Member of Technical Staff*, Bromium
<small>Jan 2012 — Jun 2013</small>
Bromium is a computer endpoint security company. The core product is vSentry providing a new approach to security, using virtualisation to secure individual user tasks from tabs in the browser to viewing documents. The first version for Windows was delivered September 2012. I worked on and ran a multitude of projects in my time at Bromium.

- Planned, implemented, and lead the team building a webservice for central computer monitoring. From planning to tested delivery in a single week useng Node.js to help the company win two major deals.

- Team lead for the development of the central webservice for controlling, monitoring and configuring the Windows computers. Initial release from planning to final tested delivery was 6 weeks using Python, Django and Windows technologies. Continuing on from to lead the next several releases on schedule defining planning, roadmap and development methodologies.

- Built a unique authenticating network stack for the virtualised web browsers. It takes web traffic from the network driver then converts it to work against authenticated proxies to ensure user credentials are not compromised.

- Developing web browsers, converting Internet Explorer and Safari into a more secure browser using virtualisation.

- Prototyped and developed the Mac OS X design for securing Safari by using the Bromium micro-virtualisation technology. Involved WebKit modification, browser extensions and native browser plugins.

- Planned, managed and delivered a major bugfix release for the platform drastically reducing customer issues with the deployment of such a complex software ecosystem.

- Provided support for customers including on-site troubleshooting.

- Bug triage, and analysis. Provided dashboards for useful visualisations for developers.

- Onboarding new developers, writing the Developer Quickstart guide. documenting and running training.

### *Software Engineer/Lead Developer/Development Manager*, Camvine (Cambridge Visual Networks)
<small>Jul 2008 — Dec 2011</small>
Camvine was a digital signage company building a new way to put data onto screens in an easy to use way. It used a web service which would control the digital signage devices based originally on custom hardware then more generic x86 hardware for high performance video. The source code for the web service and devices has since been forked by a number of companies and is still being used.  The main one is [Scene Digital](http://www.scene-digital.co.uk/).

- Worked on the original hardware and software for the client involving unique network-based frame buffers.

- Built the new version of the player running on x86 hardware to pivot the company in a very tight time period. The player was designed to be an appliance where the user would not use it as a computer.

- The digital signage player involved building an entire Linux distribution from a Ubuntu/Debian base. It involved many custom packages and running the cutting edge graphics stack to support the hardware.

- Robustness was key and it was not unusual for players to run for over 6 months with zero reboots whilst playing lots of complex content like videos and split screens.

- Built the update mechanism which was crucial for delivering the MVP fast and iterating the product rapidly without the user suffering.

- The player was built using a custom 3D compositor using Python and Clutter whilst maintaining 60fps updates.

- Supported and extended support to multiple x86 platforms.

- The test framework was built creating a virtual Internet and physical hardware running on it to test all the supported platforms. Important for ensuring updates would not break any customer machines.

- Built an LRU cache for the devices which allowed offline operation and performed authentication on NTLM corporate networks. Part of the work involved fixing the Python network stacck which I published as [coda_network](https://github.com/garrybodsworth/coda_network). Other fixes involved client certificates, socket reuse (connection: keepalive), TCP keepalive, NTLM, web auth, proxy auth, working Windows Digest auth, and a few SSL fixes so sockets can close.

- Used a variety of technologies for writing Python bindings including Boost.Python, Pyrex, Cython, ctypes and the Python C API.

- Building updated replacement packages then deploying them using the Debian APT packaging format then deploying them.

- Built a custom Webkit browser for displaying the content.

- Took over the web service development which was using Python/Django.

- Evolved the software stack into a tiered environment using Python/Django, nginx, MySQL, load-balancing and redundancy.

- Set up the SSL environment and hosting such that the web service could be rebranded for resellers whilst reusing all the same infrastructure.

- Built the new zero-downtime deployment and upgrade for continuous deployment using Python and Fabric. This allowed deployment from anywhere and also to set up new servers from scratch.

- Responsible for the unit tests (player and webservice), integration tests, the test farm and hardware, and the general running of the development process.

- Implemented the tools required for development from issue trackers, wiki documentation, source control and integration, visualisation of server status, and visualisation of the development tasks.

- Designing and researching new features across all aspects of the products and professional services.

- Providing customer support and remediation across the network of digital signage players.

- Prioritising and planning work for the development team.

- Providing the interface for sales, management and support to work with development.

- Giving the technical input for company direction.

- Performing the line manager functions for the other developers.

### *Development Engineer*, DisplayLink
<small>Jan 2008 — Jun 2008</small>


- Developing features and bugfixes as part of the release team.

- Provide the Windows Vista transition for developers.

- Ensure the product quality and release schedule working closely with the test team.

- Responsible for the bug reporting system and administering it for all teams.

- Built the framework for allowing USB ejection of devices.

### *Software Principal*, PTC (Parametric Technology Corporation)
<small>Jun 2007 — Dec 2007</small>


- Worked on Pro/TOOLMAKER CAM product which was originally NC Graphics DEPOCAM.

- Developer on the Pro/TOOLMAKER product line. This is a Windows-based CAM product which also is supplied as a library that is integrated into various large user-base third-party products.

- Initially specialised in User Interface, and 3D geometry. Involved in most areas of development.

- Improving and simplifying the development process by using better tools and processes.

- Support for other developers and the development environment. General troubleshooting.

- Extending the current OpenGL and MFC/Win32 User Interface elements for more uses.

- Implementing and testing the 64-bit version of the product including improving the build system to support it.

- Refactoring and tidying code for easier maintenance and analysis.

- Implementing performance improvements. For instance file loading speed has increased 10x.

- Working in a fully multithreaded environment.

- User interface design including icons and other raster images.

- Developing the reports output by the program, to make them configurable and easy to use.

- Researching new technologies, for example, Boost, installation programs, source control.

- Working on requirements and design. Liaising with customers and management to determine how to implement features and their feasibility.

- Understanding as much of the system as possible.

- Tools currently used include Visual Studio, Subversion, Inno Setup, STLPort, Mediawiki, ViewVC, Cygwin, PC-Lint, Parser Generator 2 (Lex and Yacc), and a variety of external libraries.

### *Software Principal*, NC Graphics (Cambridge)
<small>Aug 2005 — Jun 2007</small>


- The company no longer exists because it was taken over by Parametric Technology Corporation.  The product I worked on was DEPOCAM (also known as MSG and Tulcam). Currently exists as NCGCAM.

- Developer on DEPOCAM. Specialising in User Interface and 3D geometry.

- Extending the current OpenGL and MFC UI elements for more uses.

- Working in a fully multithreaded environment, with the core porduct also being used as a DLL.

- User interface graphical design like icons and other raster images.

- Developing the reports output by the program, to make them configurable and easy to use.

- Support for other developers in C++ and the development environment. General troubleshooting.

- Researching new technologies, eg, Boost, installation programs, source control.

### *Senior Software Engineer*, Vero International Software
<small>Sep 2002 — Jul 2005</small>


- Was taken over from NC Graphics with the Machining Strategist CAM software group.

- Developer on Machining Strategist.  Specialising in User Interface and 3D geometry.

- User interface graphical design like icons and other raster images.

- Developing the reports output by the program, to make them configurable and easy to use.

- Company-wide web based bug database – design, implementation, and technical support.

- Support for other developers in C++ and the development environment.  General troubleshooting.

- Researching new technologies.

- Batch testing.

### *Software Engineer*, NC Graphics (Cambridge)
<small>Oct 2000 — Sep 2002</small>


- Started work as a GUI developer on the MFC based product.



## Education

### University Of Essex (Oct 1999 — Aug 2000)


- BSc Computer Science - First

### University Of Essex (Oct 1996 — Jun 1999)


- MSc Computer Science - Distinction





## Recognition

### *Bowden Memorial Prize*, University Of Essex (Jun 1997)
Highest exam results

