#
# Conditional build:	
# _without_alsa - without ALSA support
#

Summary:	A general purpose sound file conversion tool
Summary(de):	Mehrzweck-Sounddatei-Konvertierungs-Tool
Summary(fr):	outil g�n�ral de conversion de fichiers son
Summary(pl):	Program do konwersji plik�w d�wi�kowych
Summary(tr):	Genel ama�l� ses dosyas� �evirme arac�
Name:		sox
Version:	12.17.3
Release:	1
License:	distributable
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	http://prdownloads.sourceforge.net/sox/%{name}-%{version}.tar.gz
Patch0:		%{name}-play.patch
Patch1:		%{name}-soundcard.patch
Patch2:		%{name}-install.patch
URL:		http://sox.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgsm-devel
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-driver-devel}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SoX (Sound eXchange) is a sound file format converter for Linux, UNIX
and DOS PCs. The self-described 'Swiss Army knife of sound tools,' SoX
can convert between many different digitized sound formats and perform
simple sound manipulation functions, including sound effects.

Install the sox package if you'd like to convert sound file formats or
manipulate some sounds.

%description -l pl
SoX (Sound eXchange) jest konwerterem format�w plik�w d�wi�kowych dla
Linuksa, Uniksa i Dosa. SoX mo�e wykonywa� konwersj� mi�dzy wieloma
formatami cyfrowego d�wi�ku. Mo�e tak�e dokonywa� prostych manipulacji
na d�wi�ku, wliczaj�c w to r�ne efekty d�wiekowe.

%package devel
Summary:	The SoX sound file format converter libraries
Summary(pl):	Biblioteka SoX do konwertowania plik�w d�wi�kowych
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����

%description devel 
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

Install sox-devel if you want to develop applications which will use
SoX.

%description devel -l pl
Ten pakiet zawiera biblioteki potrzebne do kompilacji aplikacji, kt�re
b�d� wykorzystywa�y konwerter format�w plik�w d�wi�kowych SoX.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
aclocal
autoconf
%configure \
	--with-oss-dsp \
	--with-gsm \
%ifnarch sparc sparc64
	%{!?_without_alsa:--with-alsa-dsp}
%endif

%{__make} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-lib \
	DESTDIR=$RPM_BUILD_ROOT

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/soxplay
echo "" >> $RPM_BUILD_ROOT%{_bindir}/soxplay
echo '%{_bindir}/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT%{_bindir}/soxplay

gzip -9nf Changelog README TODO INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz monkey.*
%attr(755,root,root) %{_bindir}/sox
%attr(755,root,root) %{_bindir}/soxmix
%attr(755,root,root) %{_bindir}/play   
%attr(755,root,root) %{_bindir}/rec  
%attr(755,root,root) %{_bindir}/soxplay
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libst.a
%{_includedir}/st.h
%{_mandir}/man3/*
