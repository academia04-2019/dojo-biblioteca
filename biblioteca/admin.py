from django.contrib import admin


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'lancamento', 'autor', 'genero')
    ordering = ('-lancamento',)
    search_fields = ['titulo', 'autor', 'genero']

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais', 'livro')
    search_fields = ['nome', 'pais', 'livro']
