import './App.css';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';


function App() {
  return (
    <Form action='http://localhost:5000/crawl' className='.form' method='POST'>
      <Form.Group className="mb-3">
        <Form.Label> client id: </Form.Label>
        <Form.Control name='client_id' placeholder="cliente id" required/>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label> client secret: </Form.Label>
        <Form.Control name = "client_secret" placeholder="client secret" required/>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label> username: </Form.Label>
        <Form.Control name="username" placeholder="username" required/>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label> password: </Form.Label>
        <Form.Control name="password" placeholder="password" required type="password"/>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label> user agent </Form.Label>
        <Form.Control name = "user_agent" placeholder="user agent" required/>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label> string de busca </Form.Label>
        <Form.Control name = "search_string" as = "textarea" placeholder="string de busca" required/>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label> subrredits: </Form.Label>
        <Form.Control as = "textarea" name="subreddits" placeholder="exemplo: subrredit1, subrredit2" required/>
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Check type="radio">
          <Form.Check.Input type="radio" name="tipo" value="depressivo" required/>
          <Form.Check.Label> depressivo </Form.Check.Label>
        </Form.Check>

        <Form.Check type="radio">
          <Form.Check.Input type="radio" name="tipo" value="neutro" required/>
          <Form.Check.Label> neutro </Form.Check.Label>
        </Form.Check>

      </Form.Group>
      <Button variant="primary" className="button" type="submit">
        Submit
      </Button>
    </Form>
  );
  
}

export default App;
