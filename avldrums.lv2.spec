%global		debug_package	%{nil}

Summary:		A simple Drum Sample Player Plugin
Name:	avldrums.lv2
Version:		0.7.3
Release:		1
License:		GPLv2
Group:	Sound
Url:		http://x42-plugins.com/x42/x42-avldrums
# Submodules are a pain
#Source0:	https://github.com/x42/avldrums.lv2/archive/refs/tags/v0.7.3.tar.gz
Source0:	%{name}-%{version}.tar.xz
BuildRequires:		pkgconfig(cairo)
BuildRequires:		pkgconfig(gl)
BuildRequires:		pkgconfig(glu)
BuildRequires:		pkgconfig(glib-2.0)
BuildRequires:		pkgconfig(lv2)
BuildRequires:		pkgconfig(pango)
BuildRequires:		pkgconfig(x11)

%description
This is a drum sample player plugin dedicated to Glen MacArthur's AVL
Drumkits. This self-contained plugin provides a convenient way to rapidly
sequence and mix midi-drums.
The main benefits compared to loading the soundfont into a generic sample
player are:
* built-in MIDNAM: The plugin informs the host about note-names.
* Semantic grouping of ports: fan-out separate mics to individual tracks.
* Compatible stereo/multi-out variant: it allows to in-place replace the
stereo version with multi-out. Start with stereo when sequencing and when
moving to the mixing stage use separate outputs to process or customize level
and pan of individual drums.

%files
%license COPYING
%doc README.md
%{_libdir}/lv2/%{name}

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%make_build


%install
%make_install PREFIX=%{_prefix} LV2DIR=%{_libdir}/lv2/
