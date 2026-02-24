module github.com/demo/defender-demo

go 1.18

require (
	// CVE-2022-41723: HTTP/2 DoS
	golang.org/x/net v0.0.0-20220722155237-a158d28d115b

	// CVE-2022-32149: Text DoS
	golang.org/x/text v0.3.7

	// CVE-2022-41721: HTTP/2 HPACK DoS
	golang.org/x/net v0.1.0

	// CVE-2022-27191: Crash on invalid SSH keys
	golang.org/x/crypto v0.0.0-20220314234659-1baeb1ce4c0b

	// CVE-2022-29526: syscall/js vulnerability
	golang.org/x/sys v0.0.0-20220520151302-bc2c85ada10a

	// CVE-2023-24534: HTTP & MIME header parsing
	github.com/gin-gonic/gin v1.7.7

	// CVE-2022-28948: YAML crash
	gopkg.in/yaml.v3 v3.0.0-20210107192922-496545a6307b
)
