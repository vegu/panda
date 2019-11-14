# Changelog


## unreleased

## 1.2.0
### added
- fileprobe `backlog` config option
- fileprobe `max_lines` config option
- logparse allow custom validators
- logparse `validate_interval`
- logparse `time_parser` config option
### changed
- move from `facsimile` to `ctl` for package / release management
- parse_interval now can handle multiunit strings such as 1m30s
### fixed
- mtr plugin py3 compatibility issues
- fileprobe lines that can't be processed are now skipped
- fix #62 timeseriesdb plugins crash when `update` is given `none` as a value

## 1.1.0
### added
- fileprobe plugin
- logparse plugin
- support for multiple output targets
### fixed
- python3 encoding issue in the fping module

## 1.0.1
### fixed
- ipv6 fping parsing #50

## 1.0.0
### added
- added graphite line protocol output plugin
- fping: exposed `period` parameter to config (default to 20)
- error for using duplicate probe names
### fixed
- update munge to reduce pyyaml requirements #35

## 0.6.1
### fixed
- issue where standalone vaping/vodka would not allow an fping probe to create more than one group

## 0.6.0
### added
- added python3.6 to tests
- add home_dir config option
- add better config testing
- add last time to fping
- add first iteration of mtr graph

## 0.5.0
### changed
- port to pluginmgr .5
- updated other deps
### fixed
- issue #29: python3 complains about bytes-like object in fping.py

## 0.4.0
### added
- timeseries db abstraction plugin
- whisper db plugin
- rrdtool db plugin
### fixed
- pinned pluginmgr dependency to 0.4.0 as 0.5.0 currently breaks vaping

## 0.3.0
### added
- py3 support
- better startup failure messages
- check for plugin requirements (fping, zeromq)
- added on_start() and on_stop() events to plugins
- zeromq can connect or bind to socket
### changed
- call start() on emit plugins
### fixed
- #2 error if zeromq is missing
- #3 daemonize closes plugin fds