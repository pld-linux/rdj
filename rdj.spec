Summary:	gtk+ radio program for Video4Linux users
Summary(pl):	aplikacja radiowa pod gtk+ (Video4Linux)
Summary(cs):	gtk+ radio program pro zaЬМzenМ podporujМcМ Video4Linux rozhranМ
Summary(de):	gtk+ Radio-Tuner fЭr Video4Linux-Benutzer
Summary(nl):	gtk+ radioprogramma voor gebruikers van Video4Linux
Summary(it):	gtk+ programma radio per utenti di Video4Linux
Summary(ru):	gtk+ программа для работы с радио-тюнером с использованием интерфейса Video4Linux
Name:		rdj
Version:	0.3.2
Release:	1
Vendor:		David Mimms, Jr. <tha_d@hotmail.com>
License:	GPL
Group:		X11/Applications/Multimedia
URL:		http://mimms.sourceforge.net/
Source0:	http://mimms.sourceforge.net/rdj/%{name}-%{version}.tgz
Source1:	%{name}-icons-png.tgz
Patch0:		%{name}-gettext-and-automake-support.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	gnome-libs-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
rdj is a gtk+ radio interface for bttv video devices with radio
tuners. Scanning, station editing, using devices radio0-3, setting a
default station, and having unlimited stations are fully supported.
Also, you can start your favorite television app and mixer from it.

%description -l pl
rdj jest interfejsem radiowym pod bttv u©ywaj╠cym gtk+. Program
umo©liwia skanowanie, edycjЙ listy stacji, ustawianie stacji
domy╤lnej, u©ywanie urz╠dzeЯ radio0-3. Korzystaj╠c z rdj mo©na rСwnie©
uruchomiФ swoj╠ ulubion╠ aplikacjЙ do ogl╠dania tv czy audio mikser.

%description -l cs
rdj je gtk+ rozhranМ pro bttv zaЬМzenМ s radiovЩm tunerem. Pou╬МvА
zaЬМzenМ radio0-3. Umo╬Рuje hledat a upravovat seznam dostupnЩch
stanic, nastavenМ defaultnМ stanice. Umo╬Рujue takИ spou╧tЛnМ
oblМbenИho tv programu a mixeru.

%description -l de
rdj ist ein GTK+ Radio-Tuner fЭr von BTTV unterstЭtzte
Radio/TV-Karten. Sendersuchlauf, Editieren von Sendern, Verwendung der
GerДte radio0-3, Angabe eines Standardsenders und eine unbegrenzte
Anzahl von voreingestellten Sendern werden voll unterstЭtzt. Sie
kЖnnen auъerdem eine TV-Software sowie einen Audiomixer Ihrer Wahl
starten.

%description -l nl
rdj is een gtk+ radio-interface voor bttv video apparaten met
radiotuners. Scannen, stations bewerken, gebruik van de apparaten
radio0-3, een default station instellen, en het instellen van een
onbegrensd aantal stations wordt volledig ondersteund. U kunt ook uw
favoriete televisieprogramma of mixer starten vanuit rdj.

%description -l ru
rdj --- это gtk+ программа для устройств на чипах bttv, оснащенных
радио-тюнером. Особенности: сканирование диапазона, неограниченный
редактируемый список станций, использование нескольких устройств
(radio0-3), задание станции, прослушиваемой по умолчанию. Также Вы
можете запускать Вашу любимую программу для просмотра ТВ и микшер из
rdj.


%prep
%setup -q
%patch0 -p1


%build
%{__gettextize}
aclocal
%{__autoconf}
automake -a -c

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Multimedia

install -d $RPM_BUILD_ROOT%{_pixmapsdir}

tar zxvf %{SOURCE1}
install *.png $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog COPYING KNOWN_BUGS example.rdj

%find_lang %{name} --with-gnome --all-name


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_applnkdir}/Multimedia/*
