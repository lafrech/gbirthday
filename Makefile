bindir = /usr/bin
datadir = /usr/share
pixmaps = $(datadir)/pixmaps
version = master

default:
	echo Nothing to do.

install:
	install -m 755 -d $(DESTDIR)$(datadir)/gbirthday
	install -m 755 -d $(DESTDIR)$(pixmaps)/gbirthday
	install -m 664 pics/*.png $(DESTDIR)$(pixmaps)/gbirthday/
	install -m 755  gbirthday.py $(DESTDIR)$(datadir)/gbirthday/
	install -m 755 -d $(DESTDIR)$(datadir)/gbirthday/languages/
	install -m 644 languages/*.lang \
		$(DESTDIR)$(datadir)/gbirthday/languages/
	mkdir -p $(DESTDIR)$(datadir)/applications/
	install -m 644 gbirthday.desktop $(DESTDIR)$(datadir)/applications/
	mkdir -p $(DESTDIR)$(bindir)
	install -m 755 $(DESTDIR)$(datadir)/gbirthday/gbirthday.py \
		$(DESTDIR)$(bindir)/gbirthday

uninstall:
	rm -rvf $(DESTDIR)$(datadir)/gbirthday
	rm -rvf $(DESTDIR)$(pixmaps)/gbirthday
	rm -rvf $(DESTDIR)$(datadir)/applications/gbirthday.desktop
	rm -rvf $(DESTDIR)$(bindir)/gbirthday

tar.gz:
	rm -f *.tar.gz *.tar.lzma
	tar --exclude=.git \
		-zcvf gbirthday-$(version).tar.gz *

tar.lzma:
	rm -f *.tar.lzma *.tar.gz
	tar --use-compress-program=lzma --exclude=.git \
		-cvf gbirthday-$(version).tar.lzma *
