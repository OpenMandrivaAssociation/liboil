%define name liboil
%define version 0.3.11
%define major 0.3
%define libname %mklibname oil %major
%define release %mkrel 1

Summary: Optimized functions for multimedia calculations
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.schleef.org/liboil/download/%{name}-%{version}.tar.bz2
# gw disable SSE until bug #26183 is fixed
Patch: liboil-nosse.patch
License: LGPL
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.schleef.org/liboil/
BuildRequires: gtk-doc
BuildRequires: glib2-devel
BuildRequires: automake1.9

%description
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package -n %libname
Summary: Optimized functions for multimedia calculations
Group: System/Libraries
Requires: %name-tools >= %version

%description -n %libname
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package -n %libname-devel
Summary: Optimized functions for multimedia calculations
Group: Development/C
Requires: %libname = %version
Provides: liboil-devel = %version-%release

%description -n %libname-devel
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).


%package -n %libname-static-devel
Summary: Optimized functions for multimedia calculations
Group: Development/C
Requires: %libname-devel = %version

%description -n %libname-static-devel
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package tools
Summary: Optimized functions for multimedia calculations
Group: System/Libraries

%description tools
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

This contains the binaries that are bundled with %name.

%prep
%setup -q
cd liboil
%patch
cd ..
automake

%build
%configure2_5x
#gw no parallel build please
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/liboil-%{major}.so.0*

%files -n %libname-devel
%defattr(-,root,root)
%_includedir/liboil*
%_libdir/liboil*.so
%attr(644,root,root) %_libdir/liboil*.la
%_libdir/pkgconfig/*.pc
%_datadir/gtk-doc/html/liboil

%files -n %libname-static-devel
%defattr(-,root,root)
%_libdir/liboil*.a

%files tools
%defattr(-,root,root)
%_bindir/*


