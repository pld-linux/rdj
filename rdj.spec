Summary:	gtk+ radio program for Video4Linux users
Summary(pl):	aplikacja radiowa pod gtk+ (Video4Linux)
Summary(cs):	gtk+ radio program pro za��zen� podporuj�c� Video4Linux rozhran�
Summary(de):	gtk+ Radio-Tuner f�r Video4Linux-Benutzer
Summary(nl):	gtk+ radioprogramma voor gebruikers van Video4Linux
Summary(it):	gtk+ programma radio per utenti di Video4Linux
Summary(ru):	gtk+ ��������� ��� ������ � �����-������� � �������������� ���������� Video4Linux
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
rdj jest interfejsem radiowym pod bttv u�ywaj�cym gtk+. Program
umo�liwia skanowanie, edycj� listy stacji, ustawianie stacji
domy�lnej, u�ywanie urz�dze� radio0-3. Korzystaj�c z rdj mo�na r�wnie�
uruchomi� swoj� ulubion� aplikacj� do ogl�dania tv czy audio mikser.

%description -l cs
rdj je gtk+ rozhran� pro bttv za��zen� s radiov�m tunerem. Pou��v�
za��zen� radio0-3. Umo��uje hledat a upravovat seznam dostupn�ch
stanic, nastaven� defaultn� stanice. Umo��ujue tak� spou�t�n�
obl�ben�ho tv programu a mixeru.

%description -l de
rdj ist ein GTK+ Radio-Tuner f�r von BTTV unterst�tzte
Radio/TV-Karten. Sendersuchlauf, Editieren von Sendern, Verwendung der
Ger�te radio0-3, Angabe eines Standardsenders und eine unbegrenzte
Anzahl von voreingestellten Sendern werden voll unterst�tzt. Sie
k�nnen au�erdem eine TV-Software sowie einen Audiomixer Ihrer Wahl
starten.

%description -l nl
rdj is een gtk+ radio-interface voor bttv video apparaten met
radiotuners. Scannen, stations bewerken, gebruik van de apparaten
radio0-3, een default station instellen, en het instellen van een
onbegrensd aantal stations wordt volledig ondersteund. U kunt ook uw
favoriete televisieprogramma of mixer starten vanuit rdj.

%description -l ru
rdj --- ��� gtk+ ��������� ��� ��������� �� ����� bttv, ����������
�����-�������. �����������: ������������ ���������, ��������������
������������� ������ �������, ������������� ���������� ���������
(radio0-3), ������� �������, �������������� �� ���������. ����� ��
������ ��������� ���� ������� ��������� ��� ��������� �� � ������ ��
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
