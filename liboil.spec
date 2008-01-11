%define apiver 0.3
%define major 0
%define libname %mklibname oil %{apiver} %{major}
%define develname %mklibname oil -d
%define staticname %mklibname oil -d -s

Summary:	Optimized functions for multimedia calculations
Name:		liboil
Version:	0.3.12
Release:	%mkrel 2
License:	BSD
Group:		System/Libraries
URL:		http://liboil.freedesktop.org
Source0:	http://liboil.freedesktop.org/download/%{name}-%{version}.tar.bz2
# gw disable SSE until bug #26183 is fixed
Patch:		liboil-nosse.patch
Patch1:		%{name}-0.3.12-optflags.patch
BuildRequires:	gtk-doc
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package -n %{libname}
Summary:	Optimized functions for multimedia calculations
Group:		System/Libraries
Requires:	%{name}-tools >= %{version}-%{release}
Obsoletes:	%mklibname oil 0.3
Provides:	%mklibname oil 0.3

%description -n %{libname}
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package -n %{develname}
Summary:	Optimized functions for multimedia calculations
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	liboil-devel = %{version}-%{release}
Obsoletes:	%mklibname oil 0.3 -d
Provides:	%mklibname oil 0.3 -d

%description -n %{develname}
Liboil is a library of simple functions that are optimized for various
CPUs. These functions are generally loops implementing simple
algorithms, such as converting an array of N integers to
floating-poing numbers or multiplying and summing an array of N
numbers. Clearly such functions are candidates for significant
optimization using various techniques, especially by using extended
instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).


%package -n %{staticname}
Summary:	Optimized functions for multimedia calculations
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}
Obsoletes:	%mklibname oil 0.3 -d -s
Provides:	%mklibname oil 0.3 -d -s

%description -n %{staticname}
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

This contains the binaries that are bundled with %{name}.

%prep
%setup -q
cd liboil
%patch
cd ..
%patch1 -p1

%build
./autogen.sh

# (tpg) nuke rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%configure2_5x
#gw no parallel build please
# (tpg) this dirty hack solves this :)
%(echo %make|perl -pe 's/-j\d+/-j1/g')

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liboil-%{apiver}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/liboil*
%{_libdir}/liboil*.so
%attr(644,root,root) %{_libdir}/liboil*.la
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/liboil

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/liboil*.a

%files tools
%defattr(-,root,root)
%{_bindir}/*
