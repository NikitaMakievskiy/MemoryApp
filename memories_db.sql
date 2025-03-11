--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: memory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.memory (
    id integer NOT NULL,
    text text NOT NULL,
    sentiment double precision NOT NULL
);


ALTER TABLE public.memory OWNER TO postgres;

--
-- Name: memory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.memory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.memory_id_seq OWNER TO postgres;

--
-- Name: memory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.memory_id_seq OWNED BY public.memory.id;


--
-- Name: memory id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.memory ALTER COLUMN id SET DEFAULT nextval('public.memory_id_seq'::regclass);


--
-- Data for Name: memory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.memory (id, text, sentiment) FROM stdin;
1	??? ??? ?????????? ????!	0
2	It was a shiny day!	0
\.


--
-- Name: memory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.memory_id_seq', 2, true);


--
-- Name: memory memory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.memory
    ADD CONSTRAINT memory_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

