/**
 * XXE (XML External Entity) - XML外部実体参照脆弱性
 * CodeQL Alert: java/xxe
 */
package com.demo.security;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.stream.StreamSource;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;
import java.io.StringReader;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class XmlParser {

    // ===== 脆弱性1: XXE via DocumentBuilder =====
    public Document parseXmlUnsafe(String xmlInput) throws Exception {
        // 危険: 外部エンティティ処理が有効
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        InputSource is = new InputSource(new StringReader(xmlInput));
        return builder.parse(is);
    }

    // ===== 脆弱性2: XXE via SAXParser =====
    public void parseSaxUnsafe(String xmlInput) throws Exception {
        // 危険: SAXパーサーでXXE可能
        SAXParserFactory factory = SAXParserFactory.newInstance();
        SAXParser parser = factory.newSAXParser();
        parser.parse(new InputSource(new StringReader(xmlInput)), new org.xml.sax.helpers.DefaultHandler());
    }

    // ===== 脆弱性3: XXE via TransformerFactory =====
    public void transformUnsafe(String xsltInput) throws Exception {
        // 危険: TransformerFactoryでXXE可能
        TransformerFactory factory = TransformerFactory.newInstance();
        factory.newTransformer(new StreamSource(new StringReader(xsltInput)));
    }

    // ===== 脆弱性4: XXE from HTTP Request =====
    public void handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
        // 危険: HTTPリクエストボディのXMLをそのまま解析
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document doc = builder.parse(request.getInputStream());
        String result = doc.getDocumentElement().getTextContent();
        response.getWriter().write(result);
    }
}
