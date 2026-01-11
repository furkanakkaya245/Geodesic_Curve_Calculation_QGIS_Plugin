# -*- coding: utf-8 -*-

def classFactory(iface):
    
    from .flowmap import FlowMapGenerator
    
    # QGIS arayüz nesnesini (iface) sınıfa göndererek bir örneğini döndürüyoruz.
    return FlowMapGenerator(iface)