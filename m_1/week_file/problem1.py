r = open('/home/oem/Desktop/work/directories.txt', 'w')
r.write(''' ./              .gconf/         .sudo_as_admin_successful   Видео/
 ../             .gitconfig      .swp                        Документы/
 .bash_history   .gnupg/         .var/                       Загрузки/
 .cache/         .hwdb           .viminfo                    Изображения/
 .cinnamon/      .ICEauthority   .Xauthority                 Музыка/
 .config/        .local/         .xsession-errors            Общедоступные/
 desktop/        .mozilla/       .xsession-errors.old        Шаблоны/
 Desktop/        .pki/          'Без имени 1.docx''')
r.close()
with open('/home/oem/Desktop/work/directories.txt', 'r') as f:
	print (f.read())
