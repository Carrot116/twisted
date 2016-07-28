# -*- test-case-name: twisted.python.test.test_dist3 -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Support for installing Twisted on Python 3.

Only necessary while parts of Twisted are unported.

@var modules: A list of modules that have been ported,
    e.g. "twisted.python.versions"; a package name (e.g. "twisted.python")
    indicates the corresponding __init__.py file has been ported
    (e.g. "twisted/python/__init__.py"). To reduce merge conflicts, add new
    lines in alphabetical sort.

@var testModules: A list of test modules that have been ported, e.g
    "twisted.python.test.test_versions". To reduce merge conflicts, add new
    lines in alphabetical sort.

@var testDataFiles: A list of filenames that are data files used by tests.
    These are generally used by another Python process that the test case
    spawns.

@var almostModules: A list of any other modules which are needed by any of the
    modules in the other two lists, but which themselves have not actually
    been properly ported to Python 3.  These modules might work well enough to
    satisfy some of the requirements of the modules that depend on them, but
    cannot be considered generally usable otherwise.

@var modulesToInstall: A list of all modules that should be installed on
    Python 3.
"""

from __future__ import division


modules = [
    "twisted.__init__",
    "twisted._version",
    "twisted.application.__init__",
    "twisted.application.app",
    "twisted.application.internet",
    "twisted.application.reactors",
    "twisted.application.runner.__init__",
    "twisted.application.runner._exit",
    "twisted.application.runner._runner",
    "twisted.application.runner.test.__init__",
    "twisted.application.service",
    "twisted.application.strports",
    "twisted.application.test.__init__",
    "twisted.application.twist.__init__",
    "twisted.application.twist._options",
    "twisted.application.twist._twist",
    "twisted.application.twist.test.__init__",
    "twisted.conch.__init__",
    "twisted.conch.avatar",
    "twisted.conch.checkers",
    "twisted.conch.client.__init__",
    "twisted.conch.client.knownhosts",
    "twisted.conch.error",
    "twisted.conch.interfaces",
    "twisted.conch.insults.__init__",
    "twisted.conch.insults.client",
    "twisted.conch.insults.colors",
    "twisted.conch.insults.helper",
    "twisted.conch.insults.insults",
    "twisted.conch.insults.text",
    "twisted.conch.insults.window",
    "twisted.conch.ls",
    "twisted.conch.manhole",
    "twisted.conch.manhole_tap",
    "twisted.conch.manhole_ssh",
    "twisted.conch.mixin",
    "twisted.conch.openssh_compat.__init__",
    "twisted.conch.openssh_compat.factory",
    "twisted.conch.openssh_compat.primes",
    "twisted.conch.recvline",
    "twisted.conch.scripts.__init__",
    "twisted.conch.scripts.cftp",
    "twisted.conch.scripts.ckeygen",
    "twisted.conch.scripts.conch",
    "twisted.conch.scripts.tkconch",
    "twisted.conch.ssh.__init__",
    "twisted.conch.ssh._cryptography_backports",
    "twisted.conch.ssh._kex",
    "twisted.conch.ssh.address",
    "twisted.conch.ssh.agent",
    "twisted.conch.ssh.channel",
    "twisted.conch.ssh.connection",
    "twisted.conch.ssh.common",
    "twisted.conch.ssh.factory",
    "twisted.conch.ssh.filetransfer",
    "twisted.conch.ssh.forwarding",
    "twisted.conch.ssh.keys",
    "twisted.conch.ssh.service",
    "twisted.conch.ssh.session",
    "twisted.conch.ssh.sexpy",
    "twisted.conch.ssh.transport",
    "twisted.conch.ssh.userauth",
    "twisted.conch.telnet",
    "twisted.conch.test.__init__",
    "twisted.conch.unix",
    "twisted.copyright",
    "twisted.cred.__init__",
    "twisted.cred._digest",
    "twisted.cred.checkers",
    "twisted.cred.credentials",
    "twisted.cred.error",
    "twisted.cred.portal",
    "twisted.cred.strcred",
    "twisted.cred.test.__init__",
    "twisted.enterprise.__init__",
    "twisted.enterprise.adbapi",
    "twisted.internet.__init__",
    "twisted.internet._baseprocess",
    "twisted.internet._dumbwin32proc",
    "twisted.internet._glibbase",
    "twisted.internet._newtls",
    "twisted.internet._pollingfile",
    "twisted.internet._posixstdio",
    "twisted.internet._posixserialport",
    "twisted.internet._signals",
    "twisted.internet._win32serialport",
    "twisted.internet._win32stdio",
    "twisted.internet.abstract",
    "twisted.internet.address",
    "twisted.internet.base",
    "twisted.internet.default",
    "twisted.internet.defer",
    "twisted.internet.endpoints",
    "twisted.internet.epollreactor",
    "twisted.internet.error",
    "twisted.internet.fdesc",
    "twisted.internet.gireactor",
    "twisted.internet.gtk3reactor",
    "twisted.internet.inotify",
    "twisted.internet.interfaces",
    "twisted.internet.iocpreactor.__init__",
    "twisted.internet.iocpreactor.abstract",
    "twisted.internet.iocpreactor.const",
    "twisted.internet.iocpreactor.interfaces",
    "twisted.internet.iocpreactor.reactor",
    "twisted.internet.iocpreactor.setup",
    "twisted.internet.iocpreactor.tcp",
    "twisted.internet.iocpreactor.udp",
    "twisted.internet.kqreactor",
    "twisted.internet.main",
    "twisted.internet.pollreactor",
    "twisted.internet.posixbase",
    "twisted.internet.process",
    "twisted.internet.protocol",
    "twisted.internet.reactor",
    "twisted.internet.selectreactor",
    "twisted.internet.serialport",
    "twisted.internet.ssl",
    "twisted.internet.stdio",
    "twisted.internet.task",
    "twisted.internet.tcp",
    "twisted.internet.test.__init__",
    "twisted.internet.test._posixifaces",
    "twisted.internet.test._win32ifaces",
    "twisted.internet.test.connectionmixins",
    "twisted.internet.test.fakeendpoint",
    "twisted.internet.test.modulehelpers",
    "twisted.internet.test.reactormixins",
    "twisted.internet.threads",
    "twisted.internet.udp",
    "twisted.internet.unix",
    "twisted.internet.utils",
    "twisted.internet.win32eventreactor",
    "twisted.logger.__init__",
    "twisted.logger._buffer",
    "twisted.logger._file",
    "twisted.logger._filter",
    "twisted.logger._flatten",
    "twisted.logger._format",
    "twisted.logger._global",
    "twisted.logger._io",
    "twisted.logger._json",
    "twisted.logger._legacy",
    "twisted.logger._levels",
    "twisted.logger._logger",
    "twisted.logger._observer",
    "twisted.logger._stdlib",
    "twisted.logger._util",
    "twisted.logger.test.__init__",
    "twisted.names.__init__",
    "twisted.names._rfc1982",
    "twisted.names.authority",
    "twisted.names.cache",
    "twisted.names.client",
    "twisted.names.common",
    "twisted.names.dns",
    "twisted.names.error",
    "twisted.names.hosts",
    "twisted.names.resolve",
    "twisted.names.secondary",
    "twisted.names.server",
    "twisted.names.srvconnect",
    "twisted.names.resolve",
    "twisted.names.tap",
    "twisted.names.test.__init__",
    "twisted.pair.__init__",
    "twisted.pair.raw",
    "twisted.pair.rawudp",
    "twisted.pair.test.__init__",
    "twisted.persisted.__init__",
    "twisted.persisted.aot",
    "twisted.persisted.crefutil",
    "twisted.persisted.sob",
    "twisted.persisted.styles",
    "twisted.persisted.test.__init__",
    "twisted.plugin",
    "twisted.plugins.__init__",
    "twisted.plugins.cred_anonymous",
    "twisted.plugins.cred_file",
    "twisted.plugins.cred_memory",
    "twisted.plugins.cred_sshkeys",
    "twisted.plugins.cred_unix",
    "twisted.plugins.twisted_core",
    "twisted.plugins.twisted_trial",
    "twisted.plugins.twisted_reactors",
    "twisted.plugins.twisted_web",
    "twisted.positioning.__init__",
    "twisted.positioning._sentence",
    "twisted.positioning.base",
    "twisted.positioning.ipositioning",
    "twisted.positioning.nmea",
    "twisted.positioning.test.__init__",
    "twisted.protocols.__init__",
    "twisted.protocols.amp",
    "twisted.protocols.basic",
    "twisted.protocols.policies",
    "twisted.protocols.telnet",
    "twisted.protocols.test.__init__",
    "twisted.protocols.haproxy.__init__",
    "twisted.protocols.haproxy._exceptions",
    "twisted.protocols.haproxy._info",
    "twisted.protocols.haproxy._interfaces",
    "twisted.protocols.haproxy._v1parser",
    "twisted.protocols.haproxy._v2parser",
    "twisted.protocols.haproxy._wrapper",
    "twisted.protocols.haproxy._parser",
    "twisted.protocols.haproxy.test.__init__",
    "twisted.protocols.haproxy.test.test_v1parser",
    "twisted.protocols.haproxy.test.test_v2parser",
    "twisted.protocols.haproxy.test.test_wrapper",
    "twisted.protocols.haproxy.test.test_parser",
    "twisted.protocols.socks",
    "twisted.protocols.tls",
    "twisted.python.__init__",
    "twisted.python._appdirs",
    "twisted.python._inotify",
    "twisted.python._tzhelper",
    "twisted.python._oldstyle",
    "twisted.python._shellcomp",
    "twisted.python._textattributes",
    "twisted.python._url",
    "twisted.python.compat",
    "twisted.python.components",
    "twisted.python.constants",
    "twisted.python.context",
    "twisted.python.deprecate",
    "twisted.python.dist",
    "twisted.python.dist3",
    "twisted.python.failure",
    "twisted.python.fakepwd",
    "twisted.python.filepath",
    "twisted.python.lockfile",
    "twisted.python.log",
    "twisted.python.htmlizer",
    "twisted.python.modules",
    "twisted.python.monkey",
    "twisted.python.procutils",
    "twisted.python.randbytes",
    "twisted.python.reflect",
    "twisted.python.roots",
    "twisted.python.runtime",
    "twisted.python.sendmsg",
    "twisted.python.syslog",
    "twisted.python.systemd",
    "twisted.python.test.__init__",
    "twisted.python.test.deprecatedattributes",
    "twisted.python.test.modules_helpers",
    "twisted.python.text",
    "twisted.python.threadable",
    "twisted.python.threadpool",
    "twisted.python.url",
    "twisted.python.urlpath",
    "twisted.python.usage",
    "twisted.python.util",
    "twisted.python.versions",
    "twisted.python.zippath",
    "twisted.python.zipstream",
    "twisted.scripts.__init__",
    "twisted.scripts._twistd_unix",
    "twisted.scripts._twistw",
    "twisted.scripts.test.__init__",
    "twisted.scripts.trial",
    "twisted.scripts.twistd",
    "twisted.spread.__init__",
    "twisted.spread.banana",
    "twisted.test.__init__",
    "twisted.test.iosim",
    "twisted.test.proto_helpers",
    "twisted.test.ssl_helpers",
    "twisted._threads.__init__",
    "twisted._threads._convenience",
    "twisted._threads._ithreads",
    "twisted._threads._memory",
    "twisted._threads._pool",
    "twisted._threads._team",
    "twisted._threads._threadworker",
    "twisted._threads.test.__init__",
    "twisted.trial.__init__",
    "twisted.trial._asyncrunner",
    "twisted.trial._asynctest",
    "twisted.trial._synctest",
    "twisted.trial.itrial",
    "twisted.trial.reporter",
    "twisted.trial.runner",
    "twisted.trial.test.__init__",
    "twisted.trial.test.detests",
    "twisted.trial.test.erroneous",
    "twisted.trial.test.packages",
    "twisted.trial.test.skipping",
    "twisted.trial.test.suppression",
    "twisted.trial.unittest",
    "twisted.trial.util",
    "twisted.web.__init__",
    "twisted.web._auth.__init__",
    "twisted.web._auth.basic",
    "twisted.web._auth.digest",
    "twisted.web._auth.wrapper",
    "twisted.web._element",
    "twisted.web._flatten",
    "twisted.web._newclient",
    "twisted.web._responses",
    "twisted.web._stan",
    "twisted.web.demo",
    "twisted.web.error",
    "twisted.web.guard",
    "twisted.web._http2",
    "twisted.web.http_headers",
    "twisted.web.proxy",
    "twisted.web.resource",
    "twisted.web.script",
    "twisted.web.static",
    "twisted.web.tap",
    "twisted.web.template",
    "twisted.web.test.__init__",
    "twisted.web.test.requesthelper",
    "twisted.web.util",
    "twisted.web.vhost",
    "twisted.web.wsgi",
    "twisted.web.xmlrpc",
    "twisted.words.protocols.jabber.client",
    "twisted.words.protocols.jabber.component",
    "twisted.words.protocols.jabber.error",
    "twisted.words.protocols.jabber.jid",
    "twisted.words.protocols.jabber.jstrports",
    "twisted.words.protocols.jabber.sasl",
    "twisted.words.protocols.jabber.sasl_mechanisms",
    "twisted.words.protocols.jabber.xmlstream",
    "twisted.words.protocols.jabber.xmpp_stringprep",
    "twisted.words.xish.domish",
    "twisted.words.xish.utility",
    "twisted.words.xish.xmlstream",
    "twisted.words.xish.xpath",
    "twisted.words.xish.xpathparser",
]



testModules = [
    "twisted.application.test.test_internet",
    "twisted.application.test.test_service",
    "twisted.application.runner.test.test_exit",
    "twisted.application.runner.test.test_runner",
    "twisted.application.twist.test.test_options",
    "twisted.application.twist.test.test_twist",
    "twisted.conch.test.test_address",
    "twisted.conch.test.test_agent",
    "twisted.conch.test.test_channel",
    "twisted.conch.test.test_checkers",
    "twisted.conch.test.test_connection",
    "twisted.conch.test.test_filetransfer",
    "twisted.conch.test.test_forwarding",
    "twisted.conch.test.test_insults",
    "twisted.conch.test.test_keys",
    "twisted.conch.test.test_knownhosts",
    "twisted.conch.test.test_manhole_tap",
    "twisted.conch.test.test_mixin",
    "twisted.conch.test.test_openssh_compat",
    "twisted.conch.test.test_scripts",
    "twisted.conch.test.test_session",
    "twisted.conch.test.test_ssh",
    "twisted.conch.test.test_telnet",
    "twisted.conch.test.test_text",
    "twisted.conch.test.test_transport",
    "twisted.conch.test.test_unix",
    "twisted.conch.test.test_userauth",
    "twisted.conch.test.test_window",
    "twisted.cred.test.test_cramauth",
    "twisted.cred.test.test_cred",
    "twisted.cred.test.test_digestauth",
    "twisted.cred.test.test_simpleauth",
    "twisted.cred.test.test_strcred",
    "twisted.internet.test.test_abstract",
    "twisted.internet.test.test_address",
    "twisted.internet.test.test_base",
    "twisted.internet.test.test_baseprocess",
    "twisted.internet.test.test_core",
    "twisted.internet.test.test_default",
    "twisted.internet.test.test_endpoints",
    "twisted.internet.test.test_epollreactor",
    "twisted.internet.test.test_fdset",
    "twisted.internet.test.test_filedescriptor",
    "twisted.internet.test.test_gireactor",
    "twisted.internet.test.test_glibbase",
    "twisted.internet.test.test_inlinecb",
    "twisted.internet.test.test_iocp",
    "twisted.internet.test.test_inotify",
    "twisted.internet.test.test_kqueuereactor",
    "twisted.internet.test.test_main",
    "twisted.internet.test.test_newtls",
    "twisted.internet.test.test_posixbase",
    "twisted.internet.test.test_posixprocess",
    "twisted.internet.test.test_process",
    "twisted.internet.test.test_protocol",
    "twisted.internet.test.test_serialport",
    "twisted.internet.test.test_sigchld",
    "twisted.internet.test.test_stdio",
    "twisted.internet.test.test_tcp",
    "twisted.internet.test.test_threads",
    "twisted.internet.test.test_tls",
    "twisted.internet.test.test_udp",
    "twisted.internet.test.test_udp_internals",
    "twisted.internet.test.test_unix",
    "twisted.internet.test.test_win32events",
    "twisted.logger.test.test_buffer",
    "twisted.logger.test.test_file",
    "twisted.logger.test.test_filter",
    "twisted.logger.test.test_flatten",
    "twisted.logger.test.test_format",
    "twisted.logger.test.test_global",
    "twisted.logger.test.test_io",
    "twisted.logger.test.test_json",
    "twisted.logger.test.test_legacy",
    "twisted.logger.test.test_levels",
    "twisted.logger.test.test_logger",
    "twisted.logger.test.test_observer",
    "twisted.logger.test.test_stdlib",
    "twisted.logger.test.test_util",
    "twisted.names.test.test_cache",
    "twisted.names.test.test_client",
    "twisted.names.test.test_common",
    "twisted.names.test.test_dns",
    "twisted.names.test.test_examples",
    "twisted.names.test.test_hosts",
    "twisted.names.test.test_names",
    "twisted.names.test.test_resolve",
    "twisted.names.test.test_rfc1982",
    "twisted.names.test.test_rootresolve",
    "twisted.names.test.test_server",
    "twisted.names.test.test_srvconnect",
    "twisted.names.test.test_tap",
    "twisted.names.test.test_util",
    "twisted.pair.test.test_rawudp",
    "twisted.persisted.test.test_styles",
    "twisted.positioning.test.test_base",
    "twisted.positioning.test.test_nmea",
    "twisted.positioning.test.test_sentence",
    "twisted.protocols.test.test_basic",
    "twisted.protocols.test.test_tls",
    "twisted.python.test.test_appdirs",
    "twisted.python.test.test_components",
    "twisted.python.test.test_constants",
    "twisted.python.test.test_deprecate",
    "twisted.python.test.test_dist",
    "twisted.python.test.test_dist3",
    "twisted.python.test.test_inotify",
    "twisted.python.test.test_runtime",
    "twisted.python.test.test_sendmsg",
    "twisted.python.test.test_shellcomp",
    "twisted.python.test.test_syslog",
    "twisted.python.test.test_systemd",
    "twisted.python.test.test_textattributes",
    "twisted.python.test.test_tzhelper",
    "twisted.python.test.test_url",
    "twisted.python.test.test_urlpath",
    "twisted.python.test.test_util",
    "twisted.python.test.test_versions",
    "twisted.python.test.test_zippath",
    "twisted.python.test.test_zipstream",
    "twisted.scripts.test.test_scripts",
    "twisted.test.test_abstract",
    "twisted.test.test_adbapi",
    "twisted.test.test_amp",
    "twisted.test.test_application",
    "twisted.test.test_banana",
    "twisted.test.test_compat",
    "twisted.test.test_context",
    "twisted.test.test_cooperator",
    "twisted.test.test_defer",
    "twisted.test.test_defgen",
    "twisted.test.test_error",
    "twisted.test.test_factories",
    "twisted.test.testutils",
    "twisted.test.test_failure",
    "twisted.test.test_fdesc",
    "twisted.test.test_internet",
    "twisted.test.test_iosim",
    "twisted.test.test_iutils",
    "twisted.test.test_lockfile",
    "twisted.test.test_log",
    "twisted.test.test_logfile",
    "twisted.test.test_loopback",
    "twisted.test.test_modules",
    "twisted.test.test_monkey",
    "twisted.test.test_nooldstyle",
    "twisted.test.test_paths",
    "twisted.test.test_persisted",
    "twisted.test.test_plugin",
    "twisted.test.test_policies",
    "twisted.test.test_process",
    "twisted.test.test_randbytes",
    "twisted.test.test_reflect",
    "twisted.test.test_roots",
    "twisted.test.test_sob",
    "twisted.test.test_socks",
    "twisted.test.test_ssl",
    "twisted.test.test_sslverify",
    "twisted.test.test_stdio",
    "twisted.test.test_strports",
    "twisted.test.test_task",
    "twisted.test.test_tcp",
    "twisted.test.test_tcp_internals",
    "twisted.test.test_text",
    "twisted.test.test_threadable",
    "twisted.test.test_threadpool",
    "twisted.test.test_threads",
    "twisted.test.test_tpfile",
    "twisted.test.test_twistd",
    "twisted.test.test_twisted",
    "twisted.test.test_udp",
    "twisted.test.test_unix",
    "twisted.test.test_usage",
    "twisted._threads.test.test_convenience",
    "twisted._threads.test.test_memory",
    "twisted._threads.test.test_team",
    "twisted._threads.test.test_threadworker",
    "twisted.trial.test.test_assertions",
    "twisted.trial.test.test_asyncassertions",
    "twisted.trial.test.test_deferred",
    "twisted.trial.test.test_doctest",
    "twisted.trial.test.test_keyboard",
    "twisted.trial.test.test_loader",
    "twisted.trial.test.test_log",
    "twisted.trial.test.test_output",
    "twisted.trial.test.test_plugins",
    "twisted.trial.test.test_pyunitcompat",
    "twisted.trial.test.test_reporter",
    "twisted.trial.test.test_runner",
    "twisted.trial.test.test_script",
    "twisted.trial.test.test_suppression",
    "twisted.trial.test.test_testcase",
    "twisted.trial.test.test_tests",
    "twisted.trial.test.test_util",
    "twisted.trial.test.test_warning",
    "twisted.web.test._util",
    "twisted.web.test.test_agent",
    "twisted.web.test.test_error",
    # The downloadPage tests weren't ported:
    "twisted.web.test.test_http",
    "twisted.web.test.test_http2",
    "twisted.web.test.test_flatten",
    "twisted.web.test.test_http_headers",
    "twisted.web.test.test_httpauth",
    "twisted.web.test.test_newclient",
    "twisted.web.test.test_proxy",
    "twisted.web.test.test_resource",
    "twisted.web.test.test_script",
    "twisted.web.test.test_stan",
    "twisted.web.test.test_static",
    "twisted.web.test.test_tap",
    "twisted.web.test.test_template",
    "twisted.web.test.test_util",
    "twisted.web.test.test_web",
    "twisted.web.test.test_web__responses",
    "twisted.web.test.test_webclient",
    "twisted.web.test.test_vhost",
    "twisted.web.test.test_wsgi",
    "twisted.web.test.test_xmlrpc",
    "twisted.words.test.test_domish",
    "twisted.words.test.test_jabberclient",
    "twisted.words.test.test_jabbercomponent",
    "twisted.words.test.test_jabbererror",
    "twisted.words.test.test_jabberjid",
    "twisted.words.test.test_jabberjstrports",
    "twisted.words.test.test_jabbersasl",
    "twisted.words.test.test_jabbersaslmechanisms",
    "twisted.words.test.test_jabberxmlstream",
    "twisted.words.test.test_jabberxmppstringprep",
    "twisted.words.test.test_xishutil",
    "twisted.words.test.test_xmlstream",
    "twisted.words.test.test_xpath",
]


testDataFiles = [
    "twisted.conch.test.keydata",
    "twisted.conch.test.loopback",
    "twisted.internet.test.process_cli",
    "twisted.internet.test.process_helper",
    "twisted.positioning.test.receiver",
    "twisted.python.test.pullpipe",
    "twisted.python.test.pullpipe",
    "twisted.test.mock_win32process",
    "twisted.test.plugin_basic",
    "twisted.test.plugin_extra1",
    "twisted.test.plugin_extra2",
    "twisted.test.process_cmdline",
    "twisted.test.process_echoer",
    "twisted.test.process_fds",
    "twisted.test.process_getargv",
    "twisted.test.process_getenv",
    "twisted.test.process_linger",
    "twisted.test.process_reader",
    "twisted.test.process_signal",
    "twisted.test.process_stdinreader",
    "twisted.test.process_tester",
    "twisted.test.process_tty",
    "twisted.test.process_twisted",
    "twisted.test.reflect_helper_IE",
    "twisted.test.reflect_helper_VE",
    "twisted.test.reflect_helper_ZDE",
    "twisted.test.stdio_test_consumer",
    "twisted.test.stdio_test_halfclose",
    "twisted.test.stdio_test_hostpeer",
    "twisted.test.stdio_test_lastwrite",
    "twisted.test.stdio_test_loseconn",
    "twisted.test.stdio_test_producer",
    "twisted.test.stdio_test_write",
    "twisted.test.stdio_test_writeseq",
    "twisted.trial.test.mockdoctest",
    "twisted.trial.test.moduleself",
    "twisted.trial.test.moduletest",
    "twisted.trial.test.novars",
    "twisted.trial.test.ordertests",
    "twisted.trial.test.packages",
    "twisted.trial.test.sample",
    "twisted.trial.test.scripttest",
    "twisted.trial.test.weird",
    "twisted.trial.test.mockcustomsuite",
    "twisted.trial.test.mockcustomsuite2",
    "twisted.trial.test.mockcustomsuite3",
]


almostModules = [
    # twisted.conch.test_knownhosts tests parts of the default module
    "twisted.conch.client.default",
    "twisted.conch.client.agent",
    # Required for Trial
    "twisted.python.logfile",
    # Missing test coverage, see #6156:
    "twisted.internet._sslverify",
    # twisted.names.client semi-depends on twisted.names.root, but only on
    # Windows really:
    "twisted.names.root",
    # Missing test coverage:
    "twisted.protocols.loopback",
    # Echo is ported for twisted.application tests:
    "twisted.protocols.wire",
    # Required for Trial
    "twisted.python.logfile",
    # twisted.python.filepath depends on twisted.python.win32, but on Linux it
    # only really needs to import:
    "twisted.python.win32",
    # Agent code and downloadPage aren't ported, test coverage isn't complete:
    "twisted.web.client",
    # Required by twisted.web.server, no actual code here:
    "twisted.web.iweb",
    # Required by twisted.web.server for an error handling case:
    "twisted.web.html",
    # This module has a lot of missing test coverage.  What tests it has pass,
    # but it needs a lot more.  It was ported only enough to make the client
    # work.
    "twisted.web.http",
    # GzipEncoder and allowed methods functionality not ported, no doubt
    # missing lots of test coverage:
    "twisted.web.server",
]

modulesToInstall = modules + testModules + almostModules
