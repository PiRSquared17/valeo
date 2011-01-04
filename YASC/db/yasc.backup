--
-- PostgreSQL database dump
--

-- Started on 2011-01-04 00:20:32

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 1503 (class 1259 OID 16425)
-- Dependencies: 1783 3
-- Name: tbcompra; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbcompra (
    codigo_compra integer NOT NULL,
    codigo_merc integer NOT NULL,
    codigo_prod integer NOT NULL,
    data_compra date NOT NULL,
    qtde integer,
    valor_unit numeric(15,2) DEFAULT 0,
    usuario_compra "char",
    cadastro date
);


ALTER TABLE public.tbcompra OWNER TO postgres;

--
-- TOC entry 1502 (class 1259 OID 16415)
-- Dependencies: 3
-- Name: tbmarca; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbmarca (
    codigo_marca integer NOT NULL,
    descricao_marca "char" NOT NULL
);


ALTER TABLE public.tbmarca OWNER TO postgres;

--
-- TOC entry 1500 (class 1259 OID 16402)
-- Dependencies: 3
-- Name: tbmercado; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbmercado (
    codigo_merc integer NOT NULL,
    descricao_merc "char" NOT NULL
);


ALTER TABLE public.tbmercado OWNER TO postgres;

--
-- TOC entry 1501 (class 1259 OID 16410)
-- Dependencies: 3
-- Name: tbproduto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbproduto (
    codigo_prod integer NOT NULL,
    descricao_prod "char" NOT NULL,
    marca_prod integer NOT NULL,
    cadastro_prod date,
    unidade_prod integer NOT NULL
);


ALTER TABLE public.tbproduto OWNER TO postgres;

--
-- TOC entry 1504 (class 1259 OID 16432)
-- Dependencies: 3
-- Name: tbunidade_produto; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbunidade_produto (
    codigo_unidade integer NOT NULL,
    descricao_unid "char" NOT NULL
);


ALTER TABLE public.tbunidade_produto OWNER TO postgres;

--
-- TOC entry 1505 (class 1259 OID 16454)
-- Dependencies: 3
-- Name: tbusuario; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tbusuario (
    nome "char" NOT NULL,
    senha "char" NOT NULL,
    situacao "char"
);


ALTER TABLE public.tbusuario OWNER TO postgres;

--
-- TOC entry 1812 (class 0 OID 0)
-- Dependencies: 1505
-- Name: COLUMN tbusuario.situacao; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN tbusuario.situacao IS 'A: Ativo
I: Inativo';


--
-- TOC entry 1804 (class 0 OID 16425)
-- Dependencies: 1503
-- Data for Name: tbcompra; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 1803 (class 0 OID 16415)
-- Dependencies: 1502
-- Data for Name: tbmarca; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 1801 (class 0 OID 16402)
-- Dependencies: 1500
-- Data for Name: tbmercado; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 1802 (class 0 OID 16410)
-- Dependencies: 1501
-- Data for Name: tbproduto; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 1805 (class 0 OID 16432)
-- Dependencies: 1504
-- Data for Name: tbunidade_produto; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 1806 (class 0 OID 16454)
-- Dependencies: 1505
-- Data for Name: tbusuario; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 1785 (class 2606 OID 16406)
-- Dependencies: 1500 1500
-- Name: codigo; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tbmercado
    ADD CONSTRAINT codigo PRIMARY KEY (codigo_merc);


--
-- TOC entry 1791 (class 2606 OID 16443)
-- Dependencies: 1503 1503
-- Name: codigo_compra; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tbcompra
    ADD CONSTRAINT codigo_compra PRIMARY KEY (codigo_compra);


--
-- TOC entry 1789 (class 2606 OID 16419)
-- Dependencies: 1502 1502
-- Name: codigo_marca; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tbmarca
    ADD CONSTRAINT codigo_marca PRIMARY KEY (codigo_marca);


--
-- TOC entry 1787 (class 2606 OID 16414)
-- Dependencies: 1501 1501
-- Name: codigo_prod; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tbproduto
    ADD CONSTRAINT codigo_prod PRIMARY KEY (codigo_prod);


--
-- TOC entry 1793 (class 2606 OID 16436)
-- Dependencies: 1504 1504
-- Name: codigo_unidade; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tbunidade_produto
    ADD CONSTRAINT codigo_unidade PRIMARY KEY (codigo_unidade);


--
-- TOC entry 1795 (class 2606 OID 16458)
-- Dependencies: 1505 1505
-- Name: usuario; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tbusuario
    ADD CONSTRAINT usuario PRIMARY KEY (nome);


--
-- TOC entry 1798 (class 2606 OID 16444)
-- Dependencies: 1784 1500 1503
-- Name: codigo_mercado; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tbcompra
    ADD CONSTRAINT codigo_mercado FOREIGN KEY (codigo_merc) REFERENCES tbmercado(codigo_merc);


--
-- TOC entry 1799 (class 2606 OID 16449)
-- Dependencies: 1786 1503 1501
-- Name: codigo_produto; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tbcompra
    ADD CONSTRAINT codigo_produto FOREIGN KEY (codigo_prod) REFERENCES tbproduto(codigo_prod);


--
-- TOC entry 1797 (class 2606 OID 16437)
-- Dependencies: 1504 1792 1501
-- Name: codigo_unidade; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tbproduto
    ADD CONSTRAINT codigo_unidade FOREIGN KEY (unidade_prod) REFERENCES tbunidade_produto(codigo_unidade);


--
-- TOC entry 1796 (class 2606 OID 16420)
-- Dependencies: 1502 1788 1501
-- Name: marca; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tbproduto
    ADD CONSTRAINT marca FOREIGN KEY (marca_prod) REFERENCES tbmarca(codigo_marca);


--
-- TOC entry 1800 (class 2606 OID 16459)
-- Dependencies: 1794 1503 1505
-- Name: usuario_compra; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY tbcompra
    ADD CONSTRAINT usuario_compra FOREIGN KEY (usuario_compra) REFERENCES tbusuario(nome);


--
-- TOC entry 1811 (class 0 OID 0)
-- Dependencies: 3
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2011-01-04 00:20:32

--
-- PostgreSQL database dump complete
--

