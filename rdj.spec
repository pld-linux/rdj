Summary:	GTK+ radio program for Video4Linux users
Summary(cs.UTF-8):	GTK+ radio program pro zařízení podporující Video4Linux rozhraní
Summary(de.UTF-8):	GTK+ Radio-Tuner für Video4Linux-Benutzer
Summary(it.UTF-8):	GTK+ programma radio per utenti di Video4Linux
Summary(nl.UTF-8):	GTK+ radioprogramma voor gebruikers van Video4Linux
Summary(pl.UTF-8):	Aplikacja radiowa pod GTK+ (Video4Linux)
Summary(ru.UTF-8):	GTK+ программа для работы с радио-тюнером с использованием интерфейса Video4Linux
Name:		rdj
Version:	0.3.2
Release:	1
Vendor:		David Mimms, Jr. <tha_d@hotmail.com>
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://mimms.sourceforge.net/files/%{name}-%{version}.tgz
# Source0-md5:	51d5b3d37d4ecd4db563d501f0774ca7
Source1:	%{name}-icons-png.tgz
# Source1-md5:	87f629f20233f5bf610ab4db1672cadc
Patch0:		%{name}-gettext-and-automake-support.patch
URL:		http://mimms.sourceforge.net/rdj.html
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdj is a GTK+ radio interface for bttv video devices with radio
tuners. Scanning, station editing, using devices radio0-3, setting a
default station, and having unlimited stations are fully supported.
Also, you can start your favorite television app and mixer from it.

%description -l cs.UTF-8
rdj je GTK+ rozhraní pro bttv zařízení s radiovým tunerem. Používá
zařízení radio0-3. Umožňuje hledat a upravovat seznam dostupných
stanic, nastavení defaultní stanice. Umožňujue také spouštění
oblíbeného tv programu a mixeru.

%description -l de.UTF-8
rdj ist ein GTK+ Radio-Tuner für von BTTV unterstützte
Radio/TV-Karten. Sendersuchlauf, Editieren von Sendern, Verwendung der
Geräte radio0-3, Angabe eines Standardsenders und eine unbegrenzte
Anzahl von voreingestellten Sendern werden voll unterstützt. Sie
können außerdem eine TV-Software sowie einen Audiomixer Ihrer Wahl
starten.

%description -l nl.UTF-8
rdj is een GTK+ radio-interface voor bttv video apparaten met
radiotuners. Scannen, stations bewerken, gebruik van de apparaten
radio0-3, een default station instellen, en het instellen van een
onbegrensd aantal stations wordt volledig ondersteund. U kunt ook uw
favoriete televisieprogramma of mixer starten vanuit rdj.

%description -l pl.UTF-8
rdj jest interfejsem radiowym pod bttv używającym GTK+. Program
umożliwia skanowanie, edycję listy stacji, ustawianie stacji
domyślnej, używanie urządzeń radio0-3. Korzystając z rdj można również
uruchomić swoją ulubioną aplikację do oglądania tv czy audio mikser.

%description -l ru.UTF-8
rdj --- это GTK+ программа для устройств на чипах bttv, оснащенных
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
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Multimedia

tar zxvf %{SOURCE1}
install *.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog KNOWN_BUGS README example.rdj
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_applnkdir}/Multimedia/*
