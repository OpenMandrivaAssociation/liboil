%define apiver 0.3
%define major 0
%define libname %mklibname oil %{apiver} %{major}
%define develname %mklibname oil -d
%define staticname %mklibname oil -d -s

Summary:	Optimized functions for multimedia calculations
Name:		liboil
Version:	0.3.17
Release:	2
License:	BSD
Group:		System/Libraries
URL:		http://liboil.freedesktop.org
Source0:	http://liboil.freedesktop.org/download/%{name}-%{version}.tar.gz
BuildRequires:	gtk-doc
BuildRequires:	glib2-devel

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
Requires:	%{libname} = %{version}-%{release}
Provides:	liboil-devel = %{version}-%{release}
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
Requires:	%{develname} = %{version}-%{release}
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
%attr(644,root,root) %{_libdir}/liboil*.la
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/liboil

%files -n %{staticname}
%{_libdir}/liboil*.a

%files tools
%{_bindir}/*
