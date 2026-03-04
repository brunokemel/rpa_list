### RPA -> teste de automacao com **selenium** raspagem de dados ###





***  ==>Teste pra saber em qual Iframe está meu By.NAME, "tbCategorias_length" <== ***
```bash
 for i in range(len(iframes)):
     navegador.switch_to.default_content()
     navegador.switch_to.frame(iframes[i])
    
    elementos = navegador.find_elements(By.NAME, "tbCategorias_length")
    print(f"Iframe {i} -> encontrados: {len(elementos)}")


 print(len(navegador.find_elements(By.TAG_NAME, "iframe")))

 print(len(iframes))
 ```