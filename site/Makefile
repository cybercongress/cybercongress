local="http://localhost:8080/ipfs/"
gway="https://ipfs.io/ipfs/"

zone="ipfs.io"
record="_dnslink.blog"

NPM=npm
NPMBIN=./node_modules/.bin
OUTPUTDIR=public

ifeq ($(DEBUG), true)
	PREPEND=
	APPEND=
else
	PREPEND=@
	APPEND=1>/dev/null
endif

build: clean install lint css minify
	$(PREPEND)$(NPMBIN)/hugo && \
	echo "" && \
	echo "Site built out to ./public dir"

serve: install lint js css minify
	$(PREPEND)$(NPMBIN)/hugo server

node_modules:
	$(PREPEND)$(NPM) i $(APPEND)

install: node_modules
	$(PREPEND)[ -d static/css ] || mkdir -p static/css

lint: install
	$(PREPEND)$(NPMBIN)/lessc --lint less/*

css: install
	$(PREPEND)$(NPMBIN)/lessc --clean-css --autoprefix less/main.less static/css/main.css $(APPEND)

minify: install minify-img

minify-img: install
	$(PREPEND)find static -type d -exec $(NPMBIN)/imagemin {}/* --out-dir={} $(APPEND) \; & \
	wait

dev: install css
	$(PREPEND)( \
		$(NPMBIN)/nodemon -q -e less --exec "$(NPMBIN)/lessc --clean-css --autoprefix less/main.less static/css/main.css" & \
		$(NPMBIN)/hugo server -w \
	)

clean:
	$(PREPEND)[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR) && \
	[ ! -d static/css ] || rm -rf static/css/*

publish: build
	@ipfs swarm peers >/dev/null 2>&1 || ( \
		echo "error: ipfs daemon must be online to publish"; \
		echo "try running: ipfs daemon" && exit 1)
	ipfs add -r -q public/ | tail -n1 >versions/current
	cat versions/current >>versions/history
	@export hash=`cat versions/current`; \
		echo ""; \
		echo "published blog:"; \
		echo "- $(local)$$hash"; \
		echo "- $(gway)$$hash"; \
		echo ""; \
		echo "next steps:"; \
		echo "- ipfs pin add -r /ipfs/$$hash"; \
		echo "- make publish-to-domain"; \

publish-to-github:
	./publish-to-github

# Only run after publish, or there won't be a path to set.
publish-to-domain: auth.token
	DIGITAL_OCEAN=$(shell cat auth.token) node_modules/.bin/dnslink-deploy \
		--domain=$(zone) --record=$(record) --path=/ipfs/$(shell cat versions/current)

.PHONY: build clean publish publish-to-github
