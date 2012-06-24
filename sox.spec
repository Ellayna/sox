#
# Conditional build:
%bcond_without	alsa	# without ALSA support
#
Summary:	A general purpose sound file conversion tool
Summary(de):	Mehrzweck-Sounddatei-Konvertierungs-Tool
Summary(es):	Herramienta para conversi�n de archivos de sonido
Summary(fr):	outil g�n�ral de conversion de fichiers son
Summary(pl):	Program do konwersji plik�w d�wi�kowych
Summary(pt_BR):	Ferramenta para convers�o de arquivos de som
Summary(ru):	������� ������ ���������� ��� ������ �� ��������� �������
Summary(tr):	Genel ama�l� ses dosyas� �evirme arac�
Summary(uk):	���̦�� ���������� ����������� ��� ������ �� ��������� �������
Name:		sox
Version:	12.17.9
Release:	1
License:	distributable
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/sox/%{name}-%{version}.tar.gz
# Source0-md5:	a463ef9ff2ec00007a3a42ced9572b03
Patch0:		%{name}-install.patch
URL:		http://sox.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	automake
BuildRequires:	lame-libs-devel
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SoX (Sound eXchange) is a sound file format converter for Linux, UNIX
and DOS PCs. The self-described 'Swiss Army knife of sound tools,' SoX
can convert between many different digitized sound formats and perform
simple sound manipulation functions, including sound effects.

Install the sox package if you'd like to convert sound file formats or
manipulate some sounds.

%description -l es
sox se autodenomina "navaja suiza de las herramientas de sonido".
Entiende varios formatos de sonidos digitalizados, pudiendo hacer
conversiones entre estos formatos y desempe�ar funciones sencillas de
manejo de sonido.

%description -l pl
SoX (Sound eXchange) jest konwerterem format�w plik�w d�wi�kowych dla
Linuksa, Uniksa i Dosa. SoX mo�e wykonywa� konwersj� mi�dzy wieloma
formatami cyfrowego d�wi�ku. Mo�e tak�e dokonywa� prostych manipulacji
na d�wi�ku, wliczaj�c w to r�ne efekty d�wi�kowe.

%description -l ru
��� ��������� � ������������, "����������� ��������� ��� ��������
������", sox ����� �������������� �������� ����� ����� �������������
�������� � ����������� ��������� �� ���������. � ����������� ��������
����� ����� ���� ����������� ��� ������������ �������� ������.

%description -l pt_BR
O sox se autodenomina "canivete su��o das ferramentas de som". Ele
entende v�rios formatos de sons digitalizados, podendo fazer
convers�es entre esses formatos e desempenhar fun��es simples de
manipula��o de som.

%description -l uk
� ���������æ� ��� ����� ������� "������������ ��ͦ������ �������
�������� ���̦�". ��� �ͦ� ������������ �����צ �����
���Ҧ�����Φ�Φ��� �����Ԧ� �� ���������� ��������� �� �������. �
����� ������� ������, ���� ����� ��������������� ��� �����������
�������� ���̦�.

%package devel
Summary:	The SoX sound file format converter libraries
Summary(pl):	Biblioteka SoX do konwertowania plik�w d�wi�kowych
Group:		Development/Libraries

%description devel
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

Install sox-devel if you want to develop applications which will use
SoX.

%description devel -l es
Bibliotecas que pueden ser usadas para compilar aplicaciones que usen
las bibliotecas del sox.

%description devel -l pl
Ten pakiet zawiera biblioteki potrzebne do kompilacji aplikacji, kt�re
b�d� wykorzystywa�y konwerter format�w plik�w d�wi�kowych SoX.

%description devel -l pt_BR
Bibliotecas que podem ser usadas para compilar aplica��es que usem as
bibliotecas do sox.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure \
	%{!?with_alsa:--disable-alsa-dsp}

%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-lib \
	DESTDIR=$RPM_BUILD_ROOT

echo "#!/bin/sh" > $RPM_BUILD_ROOT%{_bindir}/soxplay
echo "" >> $RPM_BUILD_ROOT%{_bindir}/soxplay
echo '%{_bindir}/sox $1 -t .au - > /dev/audio' >> $RPM_BUILD_ROOT%{_bindir}/soxplay

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/monkey.* Changelog README TODO
%attr(755,root,root) %{_bindir}/[!l]*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libst-config
%{_libdir}/libst.a
%{_includedir}/*.h
%{_mandir}/man3/*
