Summary:	Radio controller for GTK+
Summary(pl):	Kontroler radia dla GTK+
Name:		rdj
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://mimms.sourceforge.net/rdj/%{name}-%{version}.tgz
Patch0:		%{name}-X11R6_path.patch
URL:		http://mimms.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
rdj is a gtk+ radio interface for bttv video devices with radio
tuners. Scanning, station editing, using devices radio0-3, setting a
default station, and having unlimited stations are fully supported.
Also, you can start your favorite television app and mixer from it.

%description -l pl
rdj to interfejs do radia napisany w gtk+ dla urz±dzeñ wideo bttv z
tunerami radiowymi. Skanowanie, edycja stacji, u¿ywanie urz±dzeñ
radio0-3, ustawianie domy¶lnej stacji oraz nielimitowana ilo¶æ stacji
to zalety rdj. Ponadto mo¿esz uruchamiaæ dowolny program do ogl±dania
telewizji czy s³uchania radia z rdj.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
CC="%{__cc}"; export CC
%{__make} -C src rdj

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/xpm,%{_bindir},%{_mandir}/man1} \
		$RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir}}
		
install src/{rdj,rdj_scan,rdj_term,fscan} $RPM_BUILD_ROOT%{_bindir}
install rdj.desktop $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install rdj_icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install rdj.1 $RPM_BUILD_ROOT%{_mandir}/man1
install xpm/* $RPM_BUILD_ROOT%{_datadir}/%{name}/xpm

gzip -9nf KNOWN_BUGS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/rdj.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_mandir}/man?/*
