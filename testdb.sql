--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

-- Started on 2019-04-23 18:11:18 UTC

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12393)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2386 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 188 (class 1259 OID 38863)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- TOC entry 187 (class 1259 OID 38861)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- TOC entry 2387 (class 0 OID 0)
-- Dependencies: 187
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- TOC entry 190 (class 1259 OID 38873)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- TOC entry 189 (class 1259 OID 38871)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 2388 (class 0 OID 0)
-- Dependencies: 189
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- TOC entry 186 (class 1259 OID 38855)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 38853)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- TOC entry 2389 (class 0 OID 0)
-- Dependencies: 185
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- TOC entry 209 (class 1259 OID 39107)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 39105)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- TOC entry 2390 (class 0 OID 0)
-- Dependencies: 208
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- TOC entry 184 (class 1259 OID 38811)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- TOC entry 183 (class 1259 OID 38809)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- TOC entry 2391 (class 0 OID 0)
-- Dependencies: 183
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- TOC entry 182 (class 1259 OID 38800)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 38798)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- TOC entry 2392 (class 0 OID 0)
-- Dependencies: 181
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 210 (class 1259 OID 39129)
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- TOC entry 192 (class 1259 OID 38904)
-- Name: student_customuser; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_customuser (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    dept character varying(70) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.student_customuser OWNER TO postgres;

--
-- TOC entry 194 (class 1259 OID 38917)
-- Name: student_customuser_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_customuser_groups (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.student_customuser_groups OWNER TO postgres;

--
-- TOC entry 193 (class 1259 OID 38915)
-- Name: student_customuser_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_customuser_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_customuser_groups_id_seq OWNER TO postgres;

--
-- TOC entry 2393 (class 0 OID 0)
-- Dependencies: 193
-- Name: student_customuser_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_customuser_groups_id_seq OWNED BY public.student_customuser_groups.id;


--
-- TOC entry 191 (class 1259 OID 38902)
-- Name: student_customuser_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_customuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_customuser_id_seq OWNER TO postgres;

--
-- TOC entry 2394 (class 0 OID 0)
-- Dependencies: 191
-- Name: student_customuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_customuser_id_seq OWNED BY public.student_customuser.id;


--
-- TOC entry 196 (class 1259 OID 38925)
-- Name: student_customuser_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_customuser_user_permissions (
    id integer NOT NULL,
    customuser_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.student_customuser_user_permissions OWNER TO postgres;

--
-- TOC entry 195 (class 1259 OID 38923)
-- Name: student_customuser_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_customuser_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_customuser_user_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 2395 (class 0 OID 0)
-- Dependencies: 195
-- Name: student_customuser_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_customuser_user_permissions_id_seq OWNED BY public.student_customuser_user_permissions.id;


--
-- TOC entry 197 (class 1259 OID 38931)
-- Name: student_faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_faculty (
    photo character varying(100),
    empid integer NOT NULL,
    ename character varying(30) NOT NULL,
    dept character varying(70) NOT NULL,
    dob date NOT NULL,
    desig character varying(20) NOT NULL,
    permaddr text NOT NULL,
    tempaddr text NOT NULL,
    category character varying(20) NOT NULL,
    email character varying(254) NOT NULL,
    contact character varying(13) NOT NULL,
    status character varying(10) NOT NULL,
    datejoin date NOT NULL,
    dateresig date NOT NULL
);


ALTER TABLE public.student_faculty OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 38941)
-- Name: student_facultysubject; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_facultysubject (
    id integer NOT NULL,
    sem character varying(2) NOT NULL,
    branch character varying(50) NOT NULL,
    section character varying(1) NOT NULL,
    year integer NOT NULL,
    empid_id integer NOT NULL,
    subcode_id character varying(15) NOT NULL
);


ALTER TABLE public.student_facultysubject OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 38939)
-- Name: student_facultysubject_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_facultysubject_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_facultysubject_id_seq OWNER TO postgres;

--
-- TOC entry 2396 (class 0 OID 0)
-- Dependencies: 198
-- Name: student_facultysubject_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_facultysubject_id_seq OWNED BY public.student_facultysubject.id;


--
-- TOC entry 201 (class 1259 OID 38949)
-- Name: student_marklist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_marklist (
    id integer NOT NULL,
    branch character varying(70) NOT NULL,
    cursem character varying(2) NOT NULL,
    section character varying(1) NOT NULL,
    type character varying(9) NOT NULL,
    "join" integer NOT NULL,
    chance integer NOT NULL,
    mark1 smallint NOT NULL,
    mark2 smallint NOT NULL,
    mark3 smallint NOT NULL,
    mark4 smallint NOT NULL,
    subcode5 character varying(15) NOT NULL,
    mark5 smallint NOT NULL,
    subcode6 character varying(15) NOT NULL,
    mark6 smallint NOT NULL,
    markl1 smallint NOT NULL,
    markl2 smallint NOT NULL,
    subcodel3 character varying(15) NOT NULL,
    markl3 smallint NOT NULL,
    subcodel4 character varying(15) NOT NULL,
    markl4 smallint NOT NULL,
    regno_id integer NOT NULL,
    subcode1_id character varying(15) NOT NULL,
    subcode2_id character varying(15) NOT NULL,
    subcode3_id character varying(15) NOT NULL,
    subcode4_id character varying(15) NOT NULL,
    subcodel1_id character varying(15) NOT NULL,
    subcodel2_id character varying(15) NOT NULL
);


ALTER TABLE public.student_marklist OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 38947)
-- Name: student_marklist_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_marklist_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_marklist_id_seq OWNER TO postgres;

--
-- TOC entry 2397 (class 0 OID 0)
-- Dependencies: 200
-- Name: student_marklist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_marklist_id_seq OWNED BY public.student_marklist.id;


--
-- TOC entry 203 (class 1259 OID 38957)
-- Name: student_rollnoregnomap; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_rollnoregnomap (
    id integer NOT NULL,
    regno integer NOT NULL,
    rollno integer NOT NULL,
    name character varying(50) NOT NULL,
    section character varying(1) NOT NULL,
    year integer NOT NULL,
    branch character varying(50) NOT NULL,
    cursem character varying(4) NOT NULL,
    firsthr character varying(10) NOT NULL,
    secondhr character varying(10) NOT NULL,
    thirdhr character varying(10) NOT NULL,
    fourthhr character varying(10) NOT NULL,
    fifthhr character varying(10) NOT NULL,
    sixthhr character varying(10) NOT NULL,
    "time" timestamp with time zone NOT NULL,
    facultyid_id integer NOT NULL,
    subjectcode_id character varying(15) NOT NULL
);


ALTER TABLE public.student_rollnoregnomap OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 38955)
-- Name: student_rollnoregnomap_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_rollnoregnomap_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_rollnoregnomap_id_seq OWNER TO postgres;

--
-- TOC entry 2398 (class 0 OID 0)
-- Dependencies: 202
-- Name: student_rollnoregnomap_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_rollnoregnomap_id_seq OWNED BY public.student_rollnoregnomap.id;


--
-- TOC entry 204 (class 1259 OID 38963)
-- Name: student_student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_student (
    photo character varying(100),
    regno integer NOT NULL,
    name character varying(30) NOT NULL,
    branch character varying(15) NOT NULL,
    cursem character varying(2) NOT NULL,
    "join" integer NOT NULL,
    section character varying(1) NOT NULL,
    status character varying(20) NOT NULL,
    admtype character varying(20) NOT NULL,
    gender character varying(6) NOT NULL,
    admissionno integer NOT NULL,
    permanentaddress character varying(150),
    temporaryaddress character varying(150),
    dateofbirth date NOT NULL,
    category character varying(20) NOT NULL,
    emailid character varying(80),
    personwithdisabilities character varying(40),
    catrank integer NOT NULL,
    religion character varying(15),
    bloodgroup character varying(6) NOT NULL,
    parentorguardianname character varying(50),
    parentorguardianoccupation character varying(15),
    parentorguardiancontactno character varying(15),
    parentorguardianemailid character varying(50),
    miniproject character varying(100),
    miniprojectguide character varying(25),
    mainproject character varying(100),
    mainprojectguide character varying(25),
    behaviour character varying(100) NOT NULL,
    studentcontactno character varying(15),
    studentemailid character varying(50),
    tenboard character varying(20),
    tenregisterno integer,
    tenmarks integer,
    tenpercentage integer,
    tenyear integer NOT NULL,
    qualifyingboard character varying(20),
    qualifyingregisterno integer,
    qualifyingmarks integer,
    qualifyingpercentage integer,
    qualifyingyear integer,
    specialreservation character varying(30)
);


ALTER TABLE public.student_student OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 38971)
-- Name: student_subject_profile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_subject_profile (
    code character varying(15) NOT NULL,
    name character varying(70) NOT NULL,
    branch character varying(70) NOT NULL,
    sem character varying(2) NOT NULL,
    stype character varying(15) NOT NULL,
    credit integer NOT NULL,
    syllabussubid_id integer NOT NULL
);


ALTER TABLE public.student_subject_profile OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 38978)
-- Name: student_syllabus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_syllabus (
    id integer NOT NULL,
    year integer NOT NULL,
    dept character varying(60) NOT NULL,
    theory_max_internal integer NOT NULL,
    theory_max_external integer NOT NULL,
    lab_max_internal integer NOT NULL,
    lab_max_external integer NOT NULL,
    CONSTRAINT student_syllabus_lab_max_external_check CHECK ((lab_max_external >= 0)),
    CONSTRAINT student_syllabus_lab_max_internal_check CHECK ((lab_max_internal >= 0)),
    CONSTRAINT student_syllabus_theory_max_external_check CHECK ((theory_max_external >= 0)),
    CONSTRAINT student_syllabus_theory_max_internal_check CHECK ((theory_max_internal >= 0)),
    CONSTRAINT student_syllabus_year_check CHECK ((year >= 0))
);


ALTER TABLE public.student_syllabus OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 38976)
-- Name: student_syllabus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_syllabus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_syllabus_id_seq OWNER TO postgres;

--
-- TOC entry 2399 (class 0 OID 0)
-- Dependencies: 206
-- Name: student_syllabus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_syllabus_id_seq OWNED BY public.student_syllabus.id;


--
-- TOC entry 2114 (class 2604 OID 38866)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- TOC entry 2115 (class 2604 OID 38876)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 2113 (class 2604 OID 38858)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- TOC entry 2128 (class 2604 OID 39110)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- TOC entry 2112 (class 2604 OID 38814)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- TOC entry 2111 (class 2604 OID 38803)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 2116 (class 2604 OID 38907)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser ALTER COLUMN id SET DEFAULT nextval('public.student_customuser_id_seq'::regclass);


--
-- TOC entry 2117 (class 2604 OID 38920)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_groups ALTER COLUMN id SET DEFAULT nextval('public.student_customuser_groups_id_seq'::regclass);


--
-- TOC entry 2118 (class 2604 OID 38928)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.student_customuser_user_permissions_id_seq'::regclass);


--
-- TOC entry 2119 (class 2604 OID 38944)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_facultysubject ALTER COLUMN id SET DEFAULT nextval('public.student_facultysubject_id_seq'::regclass);


--
-- TOC entry 2120 (class 2604 OID 38952)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist ALTER COLUMN id SET DEFAULT nextval('public.student_marklist_id_seq'::regclass);


--
-- TOC entry 2121 (class 2604 OID 38960)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_rollnoregnomap ALTER COLUMN id SET DEFAULT nextval('public.student_rollnoregnomap_id_seq'::regclass);


--
-- TOC entry 2122 (class 2604 OID 38981)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_syllabus ALTER COLUMN id SET DEFAULT nextval('public.student_syllabus_id_seq'::regclass);


--
-- TOC entry 2355 (class 0 OID 38863)
-- Dependencies: 188
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	Faculty
2	Dataop
\.


--
-- TOC entry 2400 (class 0 OID 0)
-- Dependencies: 187
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 2, true);


--
-- TOC entry 2357 (class 0 OID 38873)
-- Dependencies: 190
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	26
2	2	32
3	2	34
4	2	35
5	2	37
6	2	38
7	2	16
8	2	17
9	2	19
10	2	20
11	2	22
12	2	23
13	2	25
14	2	26
15	2	28
16	2	29
17	2	31
\.


--
-- TOC entry 2401 (class 0 OID 0)
-- Dependencies: 189
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 17, true);


--
-- TOC entry 2353 (class 0 OID 38855)
-- Dependencies: 186
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add permission	3	add_permission
8	Can change permission	3	change_permission
9	Can delete permission	3	delete_permission
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add subject_ profile	6	add_subject_profile
17	Can change subject_ profile	6	change_subject_profile
18	Can delete subject_ profile	6	delete_subject_profile
19	Can add faculty subject	7	add_facultysubject
20	Can change faculty subject	7	change_facultysubject
21	Can delete faculty subject	7	delete_facultysubject
22	Can add student	8	add_student
23	Can change student	8	change_student
24	Can delete student	8	delete_student
25	Can add rollno regno map	9	add_rollnoregnomap
26	Can change rollno regno map	9	change_rollnoregnomap
27	Can delete rollno regno map	9	delete_rollnoregnomap
28	Can add faculty	10	add_faculty
29	Can change faculty	10	change_faculty
30	Can delete faculty	10	delete_faculty
31	Can add user	11	add_customuser
32	Can change user	11	change_customuser
33	Can delete user	11	delete_customuser
34	Can add syllabus	12	add_syllabus
35	Can change syllabus	12	change_syllabus
36	Can delete syllabus	12	delete_syllabus
37	Can add marklist	13	add_marklist
38	Can change marklist	13	change_marklist
39	Can delete marklist	13	delete_marklist
\.


--
-- TOC entry 2402 (class 0 OID 0)
-- Dependencies: 185
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 39, true);


--
-- TOC entry 2376 (class 0 OID 39107)
-- Dependencies: 209
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2019-04-23 18:01:19.720335+00	1	Faculty	1	[{"added": {}}]	2	1
2	2019-04-23 18:02:46.483333+00	2	cs_dataop	2	[{"changed": {"fields": ["groups"]}}]	11	1
3	2019-04-23 18:04:20.496728+00	2	Dataop	1	[{"added": {}}]	2	1
4	2019-04-23 18:04:47.27316+00	2	cs_dataop	2	[{"changed": {"fields": ["groups"]}}]	11	1
\.


--
-- TOC entry 2403 (class 0 OID 0)
-- Dependencies: 208
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 4, true);


--
-- TOC entry 2351 (class 0 OID 38811)
-- Dependencies: 184
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	group
3	auth	permission
4	contenttypes	contenttype
5	sessions	session
6	student	subject_profile
7	student	facultysubject
8	student	student
9	student	rollnoregnomap
10	student	faculty
11	student	customuser
12	student	syllabus
13	student	marklist
\.


--
-- TOC entry 2404 (class 0 OID 0)
-- Dependencies: 183
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- TOC entry 2349 (class 0 OID 38800)
-- Dependencies: 182
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2019-04-23 17:58:12.137031+00
2	contenttypes	0002_remove_content_type_name	2019-04-23 17:58:59.087395+00
3	auth	0001_initial	2019-04-23 17:58:59.520468+00
4	auth	0002_alter_permission_name_max_length	2019-04-23 17:58:59.553594+00
5	auth	0003_alter_user_email_max_length	2019-04-23 17:58:59.57252+00
6	auth	0004_alter_user_username_opts	2019-04-23 17:58:59.595052+00
7	auth	0005_alter_user_last_login_null	2019-04-23 17:58:59.615376+00
8	auth	0006_require_contenttypes_0002	2019-04-23 17:58:59.620311+00
9	auth	0007_alter_validators_add_error_messages	2019-04-23 17:58:59.640114+00
10	auth	0008_alter_user_username_max_length	2019-04-23 17:58:59.65992+00
11	auth	0009_alter_user_last_name_max_length	2019-04-23 17:58:59.673529+00
12	auth	0010_user_category	2019-04-23 17:58:59.693309+00
13	auth	0011_user_dept	2019-04-23 17:58:59.70668+00
14	auth	0012_remove_user_category	2019-04-23 17:58:59.726662+00
15	student	0001_initial	2019-04-23 17:59:01.680851+00
16	admin	0001_initial	2019-04-23 17:59:01.869198+00
17	admin	0002_logentry_remove_auto_add	2019-04-23 17:59:01.894796+00
18	sessions	0001_initial	2019-04-23 17:59:02.058144+00
\.


--
-- TOC entry 2405 (class 0 OID 0)
-- Dependencies: 181
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 18, true);


--
-- TOC entry 2377 (class 0 OID 39129)
-- Dependencies: 210
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- TOC entry 2359 (class 0 OID 38904)
-- Dependencies: 192
-- Data for Name: student_customuser; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, dept, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$100000$q5vLNk4TAg8i$c5mqYeMymDTS391lDP878GfKoX2ROfZrAReBN5+Vmi0=	2019-04-23 18:03:30.181243+00	t	admin			ad@gmail.com	CS	t	t	2019-04-23 18:00:11.047109+00
2	pbkdf2_sha256$100000$PRrxUxWPWKtP$cmCzxRZKY5E/lJKewatr4b8uxDWTt39kvS/3p+s9R0c=	2019-04-23 18:05:03.630129+00	f	cs_dataop	abc	jijh	sf@gmail.com	CS	f	t	2019-04-23 18:00:27+00
\.


--
-- TOC entry 2361 (class 0 OID 38917)
-- Dependencies: 194
-- Data for Name: student_customuser_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_customuser_groups (id, customuser_id, group_id) FROM stdin;
2	2	2
\.


--
-- TOC entry 2406 (class 0 OID 0)
-- Dependencies: 193
-- Name: student_customuser_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_customuser_groups_id_seq', 2, true);


--
-- TOC entry 2407 (class 0 OID 0)
-- Dependencies: 191
-- Name: student_customuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_customuser_id_seq', 2, true);


--
-- TOC entry 2363 (class 0 OID 38925)
-- Dependencies: 196
-- Data for Name: student_customuser_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2408 (class 0 OID 0)
-- Dependencies: 195
-- Name: student_customuser_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_customuser_user_permissions_id_seq', 1, false);


--
-- TOC entry 2364 (class 0 OID 38931)
-- Dependencies: 197
-- Data for Name: student_faculty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_faculty (photo, empid, ename, dept, dob, desig, permaddr, tempaddr, category, email, contact, status, datejoin, dateresig) FROM stdin;
\.


--
-- TOC entry 2366 (class 0 OID 38941)
-- Dependencies: 199
-- Data for Name: student_facultysubject; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_facultysubject (id, sem, branch, section, year, empid_id, subcode_id) FROM stdin;
\.


--
-- TOC entry 2409 (class 0 OID 0)
-- Dependencies: 198
-- Name: student_facultysubject_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_facultysubject_id_seq', 1, false);


--
-- TOC entry 2368 (class 0 OID 38949)
-- Dependencies: 201
-- Data for Name: student_marklist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_marklist (id, branch, cursem, section, type, "join", chance, mark1, mark2, mark3, mark4, subcode5, mark5, subcode6, mark6, markl1, markl2, subcodel3, markl3, subcodel4, markl4, regno_id, subcode1_id, subcode2_id, subcode3_id, subcode4_id, subcodel1_id, subcodel2_id) FROM stdin;
\.


--
-- TOC entry 2410 (class 0 OID 0)
-- Dependencies: 200
-- Name: student_marklist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_marklist_id_seq', 1, false);


--
-- TOC entry 2370 (class 0 OID 38957)
-- Dependencies: 203
-- Data for Name: student_rollnoregnomap; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_rollnoregnomap (id, regno, rollno, name, section, year, branch, cursem, firsthr, secondhr, thirdhr, fourthhr, fifthhr, sixthhr, "time", facultyid_id, subjectcode_id) FROM stdin;
\.


--
-- TOC entry 2411 (class 0 OID 0)
-- Dependencies: 202
-- Name: student_rollnoregnomap_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_rollnoregnomap_id_seq', 1, false);


--
-- TOC entry 2371 (class 0 OID 38963)
-- Dependencies: 204
-- Data for Name: student_student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_student (photo, regno, name, branch, cursem, "join", section, status, admtype, gender, admissionno, permanentaddress, temporaryaddress, dateofbirth, category, emailid, personwithdisabilities, catrank, religion, bloodgroup, parentorguardianname, parentorguardianoccupation, parentorguardiancontactno, parentorguardianemailid, miniproject, miniprojectguide, mainproject, mainprojectguide, behaviour, studentcontactno, studentemailid, tenboard, tenregisterno, tenmarks, tenpercentage, tenyear, qualifyingboard, qualifyingregisterno, qualifyingmarks, qualifyingpercentage, qualifyingyear, specialreservation) FROM stdin;
\.


--
-- TOC entry 2372 (class 0 OID 38971)
-- Dependencies: 205
-- Data for Name: student_subject_profile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_subject_profile (code, name, branch, sem, stype, credit, syllabussubid_id) FROM stdin;
\.


--
-- TOC entry 2374 (class 0 OID 38978)
-- Dependencies: 207
-- Data for Name: student_syllabus; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_syllabus (id, year, dept, theory_max_internal, theory_max_external, lab_max_internal, lab_max_external) FROM stdin;
\.


--
-- TOC entry 2412 (class 0 OID 0)
-- Dependencies: 206
-- Name: student_syllabus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_syllabus_id_seq', 1, false);


--
-- TOC entry 2143 (class 2606 OID 38870)
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 2148 (class 2606 OID 38899)
-- Name: auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 2151 (class 2606 OID 38878)
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2145 (class 2606 OID 38868)
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 2138 (class 2606 OID 38885)
-- Name: auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 2140 (class 2606 OID 38860)
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 2207 (class 2606 OID 39116)
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 2133 (class 2606 OID 38818)
-- Name: django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 2135 (class 2606 OID 38816)
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 2131 (class 2606 OID 38808)
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 2211 (class 2606 OID 39136)
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 2159 (class 2606 OID 39008)
-- Name: student_customuser_groups_customuser_id_group_id_8cf45fd5_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_groups
    ADD CONSTRAINT student_customuser_groups_customuser_id_group_id_8cf45fd5_uniq UNIQUE (customuser_id, group_id);


--
-- TOC entry 2162 (class 2606 OID 38922)
-- Name: student_customuser_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_groups
    ADD CONSTRAINT student_customuser_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 2153 (class 2606 OID 38912)
-- Name: student_customuser_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser
    ADD CONSTRAINT student_customuser_pkey PRIMARY KEY (id);


--
-- TOC entry 2164 (class 2606 OID 39022)
-- Name: student_customuser_user__customuser_id_permission_b40934ec_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_user_permissions
    ADD CONSTRAINT student_customuser_user__customuser_id_permission_b40934ec_uniq UNIQUE (customuser_id, permission_id);


--
-- TOC entry 2168 (class 2606 OID 38930)
-- Name: student_customuser_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_user_permissions
    ADD CONSTRAINT student_customuser_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2156 (class 2606 OID 38914)
-- Name: student_customuser_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser
    ADD CONSTRAINT student_customuser_username_key UNIQUE (username);


--
-- TOC entry 2170 (class 2606 OID 38938)
-- Name: student_faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_faculty
    ADD CONSTRAINT student_faculty_pkey PRIMARY KEY (empid);


--
-- TOC entry 2173 (class 2606 OID 38946)
-- Name: student_facultysubject_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_facultysubject
    ADD CONSTRAINT student_facultysubject_pkey PRIMARY KEY (id);


--
-- TOC entry 2176 (class 2606 OID 38995)
-- Name: student_facultysubject_subcode_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_facultysubject
    ADD CONSTRAINT student_facultysubject_subcode_id_key UNIQUE (subcode_id);


--
-- TOC entry 2178 (class 2606 OID 38954)
-- Name: student_marklist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist
    ADD CONSTRAINT student_marklist_pkey PRIMARY KEY (id);


--
-- TOC entry 2194 (class 2606 OID 38962)
-- Name: student_rollnoregnomap_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_rollnoregnomap
    ADD CONSTRAINT student_rollnoregnomap_pkey PRIMARY KEY (id);


--
-- TOC entry 2198 (class 2606 OID 38970)
-- Name: student_student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_student
    ADD CONSTRAINT student_student_pkey PRIMARY KEY (regno);


--
-- TOC entry 2201 (class 2606 OID 38975)
-- Name: student_subject_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subject_profile
    ADD CONSTRAINT student_subject_profile_pkey PRIMARY KEY (code);


--
-- TOC entry 2204 (class 2606 OID 38988)
-- Name: student_syllabus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_syllabus
    ADD CONSTRAINT student_syllabus_pkey PRIMARY KEY (id);


--
-- TOC entry 2141 (class 1259 OID 38887)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 2146 (class 1259 OID 38900)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 2149 (class 1259 OID 38901)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 2136 (class 1259 OID 38886)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 2205 (class 1259 OID 39127)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 2208 (class 1259 OID 39128)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 2209 (class 1259 OID 39138)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 2212 (class 1259 OID 39137)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 2157 (class 1259 OID 39009)
-- Name: student_customuser_groups_customuser_id_fa939959; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_customuser_groups_customuser_id_fa939959 ON public.student_customuser_groups USING btree (customuser_id);


--
-- TOC entry 2160 (class 1259 OID 39010)
-- Name: student_customuser_groups_group_id_dab52afe; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_customuser_groups_group_id_dab52afe ON public.student_customuser_groups USING btree (group_id);


--
-- TOC entry 2165 (class 1259 OID 39023)
-- Name: student_customuser_user_permissions_customuser_id_74ed4e22; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_customuser_user_permissions_customuser_id_74ed4e22 ON public.student_customuser_user_permissions USING btree (customuser_id);


--
-- TOC entry 2166 (class 1259 OID 39024)
-- Name: student_customuser_user_permissions_permission_id_c25fd7b6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_customuser_user_permissions_permission_id_c25fd7b6 ON public.student_customuser_user_permissions USING btree (permission_id);


--
-- TOC entry 2154 (class 1259 OID 38996)
-- Name: student_customuser_username_81b2bcf8_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_customuser_username_81b2bcf8_like ON public.student_customuser USING btree (username varchar_pattern_ops);


--
-- TOC entry 2171 (class 1259 OID 39030)
-- Name: student_facultysubject_empid_id_ca2d1af3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_facultysubject_empid_id_ca2d1af3 ON public.student_facultysubject USING btree (empid_id);


--
-- TOC entry 2174 (class 1259 OID 39099)
-- Name: student_facultysubject_subcode_id_459bddd7_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_facultysubject_subcode_id_459bddd7_like ON public.student_facultysubject USING btree (subcode_id varchar_pattern_ops);


--
-- TOC entry 2179 (class 1259 OID 39051)
-- Name: student_marklist_regno_id_3f30f90c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_regno_id_3f30f90c ON public.student_marklist USING btree (regno_id);


--
-- TOC entry 2180 (class 1259 OID 39057)
-- Name: student_marklist_subcode1_id_2da76aec; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcode1_id_2da76aec ON public.student_marklist USING btree (subcode1_id);


--
-- TOC entry 2181 (class 1259 OID 39058)
-- Name: student_marklist_subcode1_id_2da76aec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcode1_id_2da76aec_like ON public.student_marklist USING btree (subcode1_id varchar_pattern_ops);


--
-- TOC entry 2182 (class 1259 OID 39064)
-- Name: student_marklist_subcode2_id_3dcdf21c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcode2_id_3dcdf21c ON public.student_marklist USING btree (subcode2_id);


--
-- TOC entry 2183 (class 1259 OID 39065)
-- Name: student_marklist_subcode2_id_3dcdf21c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcode2_id_3dcdf21c_like ON public.student_marklist USING btree (subcode2_id varchar_pattern_ops);


--
-- TOC entry 2184 (class 1259 OID 39071)
-- Name: student_marklist_subcode3_id_975ba5cc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcode3_id_975ba5cc ON public.student_marklist USING btree (subcode3_id);


--
-- TOC entry 2185 (class 1259 OID 39072)
-- Name: student_marklist_subcode3_id_975ba5cc_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcode3_id_975ba5cc_like ON public.student_marklist USING btree (subcode3_id varchar_pattern_ops);


--
-- TOC entry 2186 (class 1259 OID 39078)
-- Name: student_marklist_subcode4_id_9eb1a869; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcode4_id_9eb1a869 ON public.student_marklist USING btree (subcode4_id);


--
-- TOC entry 2187 (class 1259 OID 39079)
-- Name: student_marklist_subcode4_id_9eb1a869_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcode4_id_9eb1a869_like ON public.student_marklist USING btree (subcode4_id varchar_pattern_ops);


--
-- TOC entry 2188 (class 1259 OID 39085)
-- Name: student_marklist_subcodel1_id_6fd2dcdd; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcodel1_id_6fd2dcdd ON public.student_marklist USING btree (subcodel1_id);


--
-- TOC entry 2189 (class 1259 OID 39086)
-- Name: student_marklist_subcodel1_id_6fd2dcdd_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcodel1_id_6fd2dcdd_like ON public.student_marklist USING btree (subcodel1_id varchar_pattern_ops);


--
-- TOC entry 2190 (class 1259 OID 39092)
-- Name: student_marklist_subcodel2_id_ec303985; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcodel2_id_ec303985 ON public.student_marklist USING btree (subcodel2_id);


--
-- TOC entry 2191 (class 1259 OID 39093)
-- Name: student_marklist_subcodel2_id_ec303985_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_marklist_subcodel2_id_ec303985_like ON public.student_marklist USING btree (subcodel2_id varchar_pattern_ops);


--
-- TOC entry 2192 (class 1259 OID 39036)
-- Name: student_rollnoregnomap_facultyid_id_8445da17; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_rollnoregnomap_facultyid_id_8445da17 ON public.student_rollnoregnomap USING btree (facultyid_id);


--
-- TOC entry 2195 (class 1259 OID 39044)
-- Name: student_rollnoregnomap_subjectcode_id_4f21e4a2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_rollnoregnomap_subjectcode_id_4f21e4a2 ON public.student_rollnoregnomap USING btree (subjectcode_id);


--
-- TOC entry 2196 (class 1259 OID 39045)
-- Name: student_rollnoregnomap_subjectcode_id_4f21e4a2_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_rollnoregnomap_subjectcode_id_4f21e4a2_like ON public.student_rollnoregnomap USING btree (subjectcode_id varchar_pattern_ops);


--
-- TOC entry 2199 (class 1259 OID 39037)
-- Name: student_subject_profile_code_34145fc5_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_subject_profile_code_34145fc5_like ON public.student_subject_profile USING btree (code varchar_pattern_ops);


--
-- TOC entry 2202 (class 1259 OID 39038)
-- Name: student_subject_profile_syllabussubid_id_c78660cc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX student_subject_profile_syllabussubid_id_c78660cc ON public.student_subject_profile USING btree (syllabussubid_id);


--
-- TOC entry 2215 (class 2606 OID 38893)
-- Name: auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2214 (class 2606 OID 38888)
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2213 (class 2606 OID 38879)
-- Name: auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2233 (class 2606 OID 39117)
-- Name: django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2232 (class 2606 OID 39122)
-- Name: django_admin_log_user_id_c564eba6_fk_student_customuser_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_student_customuser_id FOREIGN KEY (user_id) REFERENCES public.student_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2216 (class 2606 OID 38997)
-- Name: student_customuser_g_customuser_id_fa939959_fk_student_c; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_groups
    ADD CONSTRAINT student_customuser_g_customuser_id_fa939959_fk_student_c FOREIGN KEY (customuser_id) REFERENCES public.student_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2217 (class 2606 OID 39002)
-- Name: student_customuser_groups_group_id_dab52afe_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_groups
    ADD CONSTRAINT student_customuser_groups_group_id_dab52afe_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2218 (class 2606 OID 39011)
-- Name: student_customuser_u_customuser_id_74ed4e22_fk_student_c; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_user_permissions
    ADD CONSTRAINT student_customuser_u_customuser_id_74ed4e22_fk_student_c FOREIGN KEY (customuser_id) REFERENCES public.student_customuser(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2219 (class 2606 OID 39016)
-- Name: student_customuser_u_permission_id_c25fd7b6_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_customuser_user_permissions
    ADD CONSTRAINT student_customuser_u_permission_id_c25fd7b6_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2220 (class 2606 OID 39025)
-- Name: student_facultysubje_empid_id_ca2d1af3_fk_student_f; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_facultysubject
    ADD CONSTRAINT student_facultysubje_empid_id_ca2d1af3_fk_student_f FOREIGN KEY (empid_id) REFERENCES public.student_faculty(empid) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2221 (class 2606 OID 39100)
-- Name: student_facultysubje_subcode_id_459bddd7_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_facultysubject
    ADD CONSTRAINT student_facultysubje_subcode_id_459bddd7_fk_student_s FOREIGN KEY (subcode_id) REFERENCES public.student_subject_profile(code) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2222 (class 2606 OID 39052)
-- Name: student_marklist_regno_id_3f30f90c_fk_student_student_regno; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist
    ADD CONSTRAINT student_marklist_regno_id_3f30f90c_fk_student_student_regno FOREIGN KEY (regno_id) REFERENCES public.student_student(regno) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2223 (class 2606 OID 39059)
-- Name: student_marklist_subcode1_id_2da76aec_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist
    ADD CONSTRAINT student_marklist_subcode1_id_2da76aec_fk_student_s FOREIGN KEY (subcode1_id) REFERENCES public.student_subject_profile(code) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2224 (class 2606 OID 39066)
-- Name: student_marklist_subcode2_id_3dcdf21c_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist
    ADD CONSTRAINT student_marklist_subcode2_id_3dcdf21c_fk_student_s FOREIGN KEY (subcode2_id) REFERENCES public.student_subject_profile(code) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2225 (class 2606 OID 39073)
-- Name: student_marklist_subcode3_id_975ba5cc_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist
    ADD CONSTRAINT student_marklist_subcode3_id_975ba5cc_fk_student_s FOREIGN KEY (subcode3_id) REFERENCES public.student_subject_profile(code) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2226 (class 2606 OID 39080)
-- Name: student_marklist_subcode4_id_9eb1a869_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist
    ADD CONSTRAINT student_marklist_subcode4_id_9eb1a869_fk_student_s FOREIGN KEY (subcode4_id) REFERENCES public.student_subject_profile(code) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2227 (class 2606 OID 39087)
-- Name: student_marklist_subcodel1_id_6fd2dcdd_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist
    ADD CONSTRAINT student_marklist_subcodel1_id_6fd2dcdd_fk_student_s FOREIGN KEY (subcodel1_id) REFERENCES public.student_subject_profile(code) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2228 (class 2606 OID 39094)
-- Name: student_marklist_subcodel2_id_ec303985_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_marklist
    ADD CONSTRAINT student_marklist_subcodel2_id_ec303985_fk_student_s FOREIGN KEY (subcodel2_id) REFERENCES public.student_subject_profile(code) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2229 (class 2606 OID 39031)
-- Name: student_rollnoregnom_facultyid_id_8445da17_fk_student_f; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_rollnoregnomap
    ADD CONSTRAINT student_rollnoregnom_facultyid_id_8445da17_fk_student_f FOREIGN KEY (facultyid_id) REFERENCES public.student_faculty(empid) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2230 (class 2606 OID 39046)
-- Name: student_rollnoregnom_subjectcode_id_4f21e4a2_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_rollnoregnomap
    ADD CONSTRAINT student_rollnoregnom_subjectcode_id_4f21e4a2_fk_student_s FOREIGN KEY (subjectcode_id) REFERENCES public.student_subject_profile(code) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2231 (class 2606 OID 39039)
-- Name: student_subject_prof_syllabussubid_id_c78660cc_fk_student_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subject_profile
    ADD CONSTRAINT student_subject_prof_syllabussubid_id_c78660cc_fk_student_s FOREIGN KEY (syllabussubid_id) REFERENCES public.student_syllabus(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2385 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2019-04-23 18:11:18 UTC

--
-- PostgreSQL database dump complete
--

