%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define apiver 0.3
%define major 0
%define libname %mklibname oil %{apiver} %{major}
%define develname %mklibname oil -d
%define staticname %mklibname oil -d -s

Summary:	Optimized functions for multimedia calculations
Name:		liboil
Version:	0.3.17
Release:	6
License:	BSD
Group:		System/Libraries
URL:		http://liboil.freedesktop.org
Source0:	http://liboil.freedesktop.org/download/%{name}-%{version}.tar.gz
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(glib-2.0)

%description
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package -n	%{libname}
Summary:	Optimized functions for multimedia calculations
Group:		System/Libraries
Obsoletes:	%mklibname oil 0.3

%description -n	%{libname}
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package -n	%{develname}
Summary:	Optimized functions for multimedia calculations
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	oil-devel = %{EVRD}
Obsoletes:	%mklibname oil 0.3 -d

%description -n	%{develname}
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).


%package -n	%{staticname}
Summary:	Optimized functions for multimedia calculations
Group:		Development/C
Requires:	%{develname} = %{EVRD}
Obsoletes:	%mklibname oil 0.3 -d -s

%description -n %{staticname}
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package	tools
Summary:	Optimized functions for multimedia calculations
Group:		System/Libraries

%description	tools
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

This contains the binaries that are bundled with %{name}.

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
%configure2_5x

%make

%install
%makeinstall_std

%check
make check

%files -n %{libname}
%{_libdir}/liboil-%{apiver}.so.%{major}*

%files -n %{develname}
%{_includedir}/liboil*
%{_libdir}/liboil*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/liboil

%files -n %{staticname}
%{_libdir}/liboil*.a

%files tools
%{_bindir}/*


%changelog
* Mon May 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.17-4
+ Revision: 797222
- rebuild

* Sat Dec 03 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.17-3
+ Revision: 737504
- update to use pkgconfig() buildrequires
- use %%{EVRD} macro
- canonicalize provides: s/liboil-devel/oil-devel/
- cosmetics
- remove legacy rpm stuff
- remove deprecated ldconfig scriptlets
- fix dependency loop

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.17-2mdv2011.0
+ Revision: 609765
- rebuild

* Sat Mar 20 2010 Emmanuel Andry <eandry@mandriva.org> 0.3.17-1mdv2010.1
+ Revision: 525482
- New version 0.3.17

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.16-3mdv2010.1
+ Revision: 520893
- rebuilt for 2010.1

* Sun May 03 2009 Götz Waschk <waschk@mandriva.org> 0.3.16-2mdv2010.0
+ Revision: 371110
- bump
- new version

* Thu Jul 03 2008 Götz Waschk <waschk@mandriva.org> 0.3.15-1mdv2009.0
+ Revision: 230892
- new version

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Frederic Crozat <fcrozat@mandriva.com> 0.3.14-1mdv2009.0
+ Revision: 214302
- Release 0.3.14
- enable make check

* Wed Feb 27 2008 Frederic Crozat <fcrozat@mandriva.com> 0.3.13-1mdv2008.1
+ Revision: 175919
- Release 0.3.13
- Remove patch0, merged upstream

* Tue Feb 19 2008 Frederic Crozat <fcrozat@mandriva.com> 0.3.12-5mdv2008.1
+ Revision: 173065
- Fix build in iurt
- Disable omit-frame-pointer, it is crashing SSE detection when called from Mono (fd.o bug #8529)
- Remove patch0, enable back SSE support
- Remove patch1, not needed at all

* Thu Jan 17 2008 Götz Waschk <waschk@mandriva.org> 0.3.12-4mdv2008.1
+ Revision: 153994
- fix dep of the static devel package
- remove useless provides

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jan 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.12-2mdv2008.1
+ Revision: 147997
- correct license is BSD in this case
- new devel library policy
- correct libification
- use hack for parallel build
- fix mixture of tabs and spaces
- compile liboil with %%optflags (p1)
- remove rpath
- drop buildrequires on automake1.9

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 29 2007 Götz Waschk <waschk@mandriva.org> 0.3.12-1mdv2008.0
+ Revision: 32635
- new version

* Mon Apr 23 2007 Götz Waschk <waschk@mandriva.org> 0.3.11-1mdv2008.0
+ Revision: 17173
- new version

