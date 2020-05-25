%global debug_package %{nil}

Name:           fd
Version:        8.1.1
Release:        1%{?dist}
Summary:        fd is a simple, fast and user-friendly alternative to find.
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/sharkdp/%{name}
Source:         https://github.com/sharkdp/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake, libgit2, openssl-devel, cargo, rust

%description
- Convenient syntax: fd PATTERN instead of find -iname '*PATTERN*'.
- Colorized terminal output (similar to ls).
- It's fast (see benchmarks below).
- Smart case: the search is case-insensitive by default. It switches to case-sensitive if the pattern contains an uppercase character*.
- Ignores hidden directories and files, by default.
- Ignores patterns from your .gitignore, by default.
- Regular expressions.
- Unicode-awareness.
- The command name is 50 percent shorter* than find :-).
- Parallel command execution with a syntax similar to GNU Parallel.

%prep
%setup -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/fd %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
/usr/bin/fd

%changelog
* Tue May 26 2020 Jamie Curnow <jc@jc21.com> - 8.1.1-1
- v8.1.1

* Wed May 20 2020 Jamie Curnow <jc@jc21.com> - 8.1.0-1
- v8.1.0

* Fri Apr 17 2020 Jamie Curnow <jc@jc21.com> - 8.0.0-1
- v8.0.0

* Tue Mar 24 2020 Jamie Curnow <jc@jc21.com> - 7.5.0-1
- v7.5.0

* Mon Sep 16 2019 Jamie Curnow <jc@jc21.com> - 7.4.0-1
- v7.4.0

* Thu Feb 14 2019 Jamie Curnow <jc@jc21.com> - 7.3.0-1
- v7.3.0 <3

* Mon Oct 29 2018 Jamie Curnow <jc@jc21.com> - 7.2.0-1
- v7.2.0

* Fri Aug 31 2018 Jamie Curnow <jc@jc21.com> - 7.1.0-1
- Initial spec

